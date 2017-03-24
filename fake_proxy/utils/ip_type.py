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

import re
import json
import time

import requests
from pif import get_public_ip
from fake_useragent import UserAgent

from fake_proxy.config import config

url = "http://httpbin.org/ip"
ua_cls = UserAgent()
config = config.get("default")


def ip_type(proxy, headers=config.headers, start_time=time.time()):
    """ 确定代理ip的类型, 并记录响应时间
    :param proxy: 代理ip
    :param headers: 默认headers
    :return:
    """
    if not isinstance(proxy, dict):
        raise Exception("Error, <%s> argument error.")
    proxy_ip = re.search("(\d{1,3}.){3}\d{1,3}", proxy.values()[0]).group()
    headers["User-Agent"] = ua_cls.random
    headers["X_FORWARDED_FOR"] = proxy_ip
    res = requests.get(url=url, headers=headers, proxies=proxy)
    proxy_cst = "%.3f" % (time.time() - start_time)
    http_via = res.headers.get("Via", "").strip()                               # HTTP_VIA
    remote_addr = json.loads(res.text).get("origin", "").split(',')[-1].strip() # REMOTE_ADDR, record the last ip
    http_x_forwarded_for = json.loads(res.text).get("origin", "").strip()       # HTTP_X_FORWARDED_FOR, record all ips
    orig_addr = get_public_ip().strip()                                         # real ip

    print remote_addr
    print http_x_forwarded_for
    print orig_addr

    # 代理类型说明:
    # transparent(透明代理), anonymous(匿名代理), elite(高匿代理), nothing(无代理)

    if remote_addr == proxy_ip and http_via == proxy_ip and http_x_forwarded_for == orig_addr:
        proxy_type = "transparent"
    elif remote_addr == proxy_ip and http_via == proxy_ip and http_x_forwarded_for == proxy_ip:
        proxy_type = "anonymous"
    elif remote_addr == proxy_ip and http_via == "" and http_x_forwarded_for == "":
        proxy_type = "elite"
    else:
        proxy_type = "nothing"

    return proxy_type, proxy_cst

if __name__ == '__main__':
    proxy = {
        "http": "http://123.57.38.250:9898"
    }
    print ip_type(proxy)

