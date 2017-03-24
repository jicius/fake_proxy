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

from fake_proxy import db


class HttpProxy(db.Document):
    """ 代理-http代理数据库

    默认协议为http, 代理类型为透明,
    """
    ip = db.StringField(required=True, unique=True)    # ip
    port = db.IntField(required=True)                  # 端口号
    protocol = db.StringField(default="http")          # 协议类型, http, https, socks
    ptype = db.StringField(default="transparent")      # 代理类型, 透明(transparent), 匿名(anonymous), 高匿(elite)
    times = db.IntField(default=0)                     # 调用次数
    survival = db.IntField(default=0)                  # 存活时间, 单位分钟
    active = db.IntField(default=0)                    # 是否存活, 默认为0表示非存活, 1表示存活
    created = db.IntField(default=int(time.time()))    # 入库时间戳, 作为proxy出生时间
    source = db.StringField(default=u"免费代理网")      # 来源, 用来标识网站, 格式"中文名.英文名"
    pdetail = db.StringField()                         # ip详细信息
    datetime = db.StringField(default=str(datetime.datetime.now()))       # 上次验证时间