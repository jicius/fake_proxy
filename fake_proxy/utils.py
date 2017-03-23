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

import re
import json

import requests


query_ip_area_api = "http://ip.taobao.com/service/getIpInfo.php?ip=%s"


def fetch_area(proxy):
    """ 调用taobao接口返回ip详细信息 """
    ip = re.search("(\d{1,3}.){3}\d{1,3}", proxy)
    text, result = None, "{'ip': '%s'}" % ip
    if not ip:
        pass
    else:
        url = query_ip_area_api % ip.group()
        text = requests.get(url).text
    if not text:
        pass
    else:
        result = text
    return json.loads(result).get("data")


if __name__ == '__main__':
    proxy = "http://123.57.38.250:9898"
    print fetch_area(proxy)