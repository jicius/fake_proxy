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

import scrapy

from fake_proxy.config import crawl_name
from fake_proxy.utils.parse_cfg import parse_cfg


class ProxySpider(scrapy.Spider):
    name = crawl_name

    def start_requests(self):
        cfg = parse_cfg()
        if cfg.has_key("websites"):
            urls = cfg.get("websites")
        else:
            raise Exception("Error, website.yml websites not exist")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = response.body
