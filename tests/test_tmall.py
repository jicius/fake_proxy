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

import json
import requests


def fetch(url):
    body = requests.get(url).text
    item = json.loads(body)
    print time.ctime(), item.get('total_results')


if __name__ == '__main__':
    url = 'http://s.m.tmall.com/m/search_items.htm?page_size=100&page_no=1&cat=55398003&sort=d'
    for _ in range(1000):
        fetch(url=url)
        time.sleep(10)

