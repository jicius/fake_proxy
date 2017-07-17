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

import rollbar


token = "3723a904a3a4452fa2acf076bc971aa5"

rollbar.init(token)

for _ in range(10):
    try:
        raise Exception("2")
    except Exception as e:
        rollbar.report_message(e, level="error")

    # rollbar.report_message(u"失败", level="info")