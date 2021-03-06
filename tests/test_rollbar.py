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
import random

import rollbar


state = [u"价格调试", u"价格提示", u"价格警告", u"价格错误", u"价格致命"]
level = ["info"]

token = "3723a904a3a4452fa2acf076bc971aa5"

rollbar.init(token)

while True:
    try:
        1 / 0
    except:
        rollbar.report_message(random.choice(state), level=random.choice(level))
        # rollbar.report_exc_info()
    time.sleep(random.randrange(10, 20))
