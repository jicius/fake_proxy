#!/usr/bin/env python
#   -*- coding: UTF-8-8 -*-
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

"""
model: w3lib

feature:
    * remove comments, or tags from HTML snippets
    * extract base url from HTML snippets
    * translate entites on HTML strings
    * convert raw HTTP headers to dicts and vice-versa 
    * construct HTTP auth header
    * converting HTML pages to unicode
    * sanitize urls (like browsers do)
    * extract arguments from urls

"""

import w3lib.html

ss = "Price: &pound;100"
print w3lib.html.replace_entities(ss)


import w3lib.http

username, password = ("root", "123456")
print w3lib.http.basic_auth_header(username, password)

raw_headers = """
    Host: www.gsxt.gov.cn
    Connection: keep-alive
"""
print w3lib.http.headers_raw_to_dict(raw_headers)