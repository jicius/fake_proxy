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

import os

crawl_name = "proxy_spider"
project_name = "fake_proxy"
project_cfg_file = "website.yml"
project_dir_path = "/Users/Jicius/Git/fake_proxy"
project_pkg_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Upgrade-Insecure-Requests": "1"
    }

    def __ini__(self):
        pass


class DevelopmentConfig(Config):
    mongodb_setting = {
        'DB': 'arbitrary',
        'HOST': '192.168.1.214',
        'PORT': 37019,
        'USERNAME': 'guest',
        'PASSWORD': '8df12346609643d6a595faeae99e6ce0'
    }

    sqlite_setting = {

    }

    domain = "https://www.baidu.com"


class TestingConfig(Config):
    mongodb_setting = {
        'DB': 'arbitrary',
        'HOST': '192.168.1.214',
        'PORT': 37019,
        'USERNAME': 'guest',
        'PASSWORD': '8df12346609643d6a595faeae99e6ce0'
    }
    sqlite_setting = {

    }


class ProductionConfig(Config):
    mongodb_setting = {
        'DB': 'arbitrary',
        'HOST': '127.0.0.1',
        'PORT': 37019,
        'USERNAME': 'guest',
        'PASSWORD': '8df12346609643d6a595faeae99e6ce0'
    }

    sqlite_setting = {

    }


config_setting = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
<<<<<<< HEAD

config = config_setting.get(os.getenv('ENVIRONMENT'), DevelopmentConfig)
=======
>>>>>>> 5775b5c346517958bde4c2a6d3ddce320ab9a937
