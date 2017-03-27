#!/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#   Copyright (C) 2017 Jicius
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
import Queue
import sys

import requests

from fake_proxy.config import config
from fake_proxy.models import HttpProxy

queue = Queue.Queue()
config = config.get("default")


class FakeHttpProxy(object):
    def __init__(self, domain=None, pool=queue, interval=1*60):
        self.domain = domain
        self.proxies_pool = pool
        self.interval = interval            # 刷新pool时间间隔, 默认1*60分钟
        self.meta = dict()
        self.init_pool()

    def init_pool(self):
        """ 初始化代理池 """
        self._update()
        items = self._query(active=1)
        self.meta["proxies"] = list()
        for it in items:
            self.meta["proxies"].append(it)
            self.proxies_pool.put(self._proxy(it.protocol, it.ip, it.port))

    def _validate(self, proxy):
        """ 代理池代理有效性检测 """
        return requests.get(self.domain, proxies=proxy).status_code == 200

    def _update(self):
        """ 更新代理状态 """
        active = 1 if self.domain else 0
        proxies = self._query(active=active)
        for it in proxies:
            proxy = self._proxy(it.protocol, it.ip, it.port)
            res = requests.get(self.domain, headers=config.headers, proxies=proxy)
            active, ptype, survival = 0, "transparent", 0
            if not res.is_redirect:
                active = 1                  # 设为存活状态
                survival = (int(time.time())-it.created) / 60
            else:
                ptype = "nothing"           # 修改代理代理类型为无效代理
            it.update(
                active=active,
                ptype=ptype,
                times=it.times+1,
                survival=survival,
                datetime=str(datetime.datetime.now())
            )

    def _query(self, active=0):
        """ 加载数据库中的代理ip
    
        :param active: active为0表示代理无效，1表示代理有效
        :return: 
        """
        items = HttpProxy.objects(active=active).all()
        for it in items:
            yield it

    def refresh(self):
        """ 定期刷新池子中的代理 """
        pass

    def do_get(self, proxy_type=None):
        """ 代理出队列 
        
        默认按照队列特性代理random，支持type筛选
        """
        while not self.proxies_pool.empty():
            proxy = self.proxies_pool.get()
            if not proxy_type:
                pass
            elif self.do_filter(proxy=proxy, proxy_type=proxy_type):
                pass
            else:
                self.do_put(proxy, check_enable=False)
                return
            self.do_put(proxy, check_enable=False)
            return proxy

    def do_put(self, proxy, check_enable=False):
        """ 代理入队列

        如果check_enable为True, 则每次入队列前, 检测有效性, 无效出队列
        如果为False则只做加载操作, 库中ip状态由最近一次更新决定
        """
        if not check_enable:
            self.proxies_pool.put(proxy)
        else:
            if self._validate(proxy):
                self.proxies_pool.put(proxy)

    def do_filter(self, proxy, proxy_type):
        for each_proxy in self.meta["proxies"]:
            tmp_proxy = self._proxy(each_proxy.protocol, each_proxy.ip, each_proxy.port)
            if tmp_proxy == proxy and each_proxy.ptype == proxy_type:
                return True

    def _proxy(self, protocol, ip, port):
        """  格式化返回代理ip """
        return {"%s" % protocol: "%s://%s:%s" % (protocol, ip, str(port))}

    @property
    def transparent(self):
        """ 返回透明代理 """
        return self.do_get(proxy_type=sys._getframe().f_code.co_name)

    @property
    def anonymous(self):
        """ 返回匿名代理 """
        return self.do_get(proxy_type=sys._getframe().f_code.co_name)

    @property
    def elite(self):
        """ 返回高匿代理 """
        return self.do_get(proxy_type=sys._getframe().f_code.co_name)

    @property
    def random(self):
        """ 返回随机代理 """
        return self.do_get()


# # common alias
# HttpProxy = FakeHttpProxy

if __name__ == '__main__':

    hp_cls = FakeHttpProxy(domain=config.domain)
    print hp_cls.random
    print hp_cls.transparent
    print hp_cls.anonymous
    print hp_cls.elite
