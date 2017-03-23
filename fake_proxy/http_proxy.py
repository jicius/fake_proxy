#!/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#   Copyright (C) 2017 omega
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import datetime
import random
import Queue
from multiprocessing.dummy import Pool as ThreadPool
import requests

from omega.config import config
from omega.models import HttpProxy

queue = Queue.Queue()
config = config.get("default")


class FakeHttpProxy(object):
    def __init__(self, domains=None, pool=queue, interval=1*60):
        self.domains = domains
        self.proxies_pool = pool
        self.interval = interval            # 刷新pool时间间隔, 默认1*60分钟

    def init_pool(self):
        if not domains:
            items = self._query(active=0)
        else:
            items = self._query(active=1)
        for it in items:
            proxy = {"%s" % it.protocol: "%s://%s:%s" % (it.protocol, it.ip, str(it.port))}
            self.proxies_pool.put(proxy)

    def _validate(self, thread_pool_size=4):
        if not self.domains:
            pass                 # 默认对所有domains可用
        else:
            pool = ThreadPool(thread_pool_size)
            pool.map(self._update, self.domains)
            pool.close()
            pool.join()

    def _update(self, url):
        proxies = self._query()
        for it in proxies:
            proxy = {"%s" % it.protocol: "%s://%s:%s" % (it.protocol, it.ip, str(it.port))}
            res = requests.get(url, headers=config.headers, proxies=proxy)
            active, ptype, survival = 0, "anonymous", 0
            if not res.is_redirect:
                active = 1                  # 设为存活状态
                survival = (int(time.time())-it.created) / 60
            else:
                ptype = "transparent"       # 代理修改为透明
            it.update(
                active=active,
                ptype=ptype,
                times=it.times+1,
                survival=survival,
                datetime=str(datetime.datetime.now())
            )

    def _query(self, active=0):
        items = HttpProxy.objects(active=active).all()
        for it in items:
            yield it

    def loop_reload(self):
        """ 根据interval将代理加载到队列中 """
        pass

    def do_get(self, type="random"):
        while not self.proxies_pool.empty():
            proxy = self.proxies_pool.get()
            self.do_put(proxy, check_enable=False)
            return proxy

    def do_put(self, proxy, check_enable=False):
        """ 代理如队列

        如果check_enable为True, 则每次入队列前, 检测有效性, 无效出队列
        如果为False则只做加载操作, 库中ip状态由最近一次更新决定
        """
        if not check_enable:
            self.init_pool()
        else:
            # TODO 及时更新
            pass

    @property
    def transparent(self):
        """ 透明代理

        透明代理可以直接'隐藏'你的代理, 其中REMOTE_ADDR=Proxy IP, HTTP_VIA=Proxy Ip,
        但是可以通过HTTP_X_FORWARDED_FOR来追查
        """
        return self.do_get(type="transparent")

    @property
    def anonymous(self):
        """ 匿名代理

        使用匿名代理, 别人知道你使用了代理, 但是不知道你是谁, HTTP_X_FORWARDED_FOR指向proxy_ip
        """
        return self.do_get(type="anonymous")

    @property
    def distorting(self):
        """ 混淆代理

        混淆代理比匿名代理高明, 别人知道你在用代理, 但是会得到一个假的ip, HTTP_X_FORWARDED_FOR指向random_ip
        """
        return self.do_get(type="distorting")

    @property
    def elite(self):
        """ 高匿代理

        高匿代理无法让人发现你在用代理, REMOTE_ADDR=Proxy IP, REMOTE_ADDR=Proxy IP,
         HTTP_X_FORWARDED_FOR=not determined
        """
        return self.do_get(type="elite")

    @property
    def random(self):
        """ 随机代理 """
        return self.do_get()


# # common alias
# HttpProxy = FakeHttpProxy

if __name__ == '__main__':
    domains = config.proxy_domains

    hp_cls = FakeHttpProxy(domains=config.proxy_domains)
    hp_cls._validate()
