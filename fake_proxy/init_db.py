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

import json
import mongoengine

from omega.models import HttpProxy
from omega.fake_proxy.utils import fetch_area


# squid 代理
proxies = [
    {"http": "http://123.57.38.250:9898"},
    {"http": "http://123.57.138.185:9898"},
    {"http": "http://123.57.51.62:9898"},
    {"http": "http://182.92.11.155:9898"},
    {"http": "http://123.56.134.223:9898"},
    {"http": "http://123.56.106.254:9898"},
    {"http": "http://202.85.213.18:9898"},
    {"http": "http://202.85.213.17:9898"},
    {"http": "http://101.200.173.27:9898"},
    {"http": "http://103.235.243.154:9898"},
    {"http": "http://123.57.60.143:9898"},
    {"http": "http://111.202.120.112:9898"},
    {"http": "http://103.237.0.89:9898"},
    {"http": "http://103.237.0.91:9898"},
    {"http": "http://103.237.0.92:9898"},
]


if __name__ == '__main__':
    for each_proxy in proxies:
        proxy = each_proxy.get("http")
        ip_port = proxy.replace("http://", "").split(":")
        ip, port = ip_port[0], ip_port[1]
        print ip, port
        try:
            HttpProxy(
                ip=ip,
                port=int(port),
                protocol="http".lower(),
                ptype="anonymous",
                source=u"squid代理",
                pdetail=json.dumps(fetch_area(proxy)).decode("unicode_escape")
            ).save()
        except mongoengine.errors.NotUniqueError:
            print "duplicate key error collection: arbitrary.proxy index"
