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


import requests


url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?r=1498715873280&seq=0&skey=@crypt_a2aab4f1_62c63c4e843fff0f07eacbaf64e902cf"

headers = {
    "Host": "wx.qq.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "Cookie": "RK=+asbCrR7Vy; pgv_pvi=7762283520; pgv_pvid=6187606236; o_cookie=487834315; pac_uid=1_487834315; pgv_si=s4650082304; webwxuvid=e9bcaecf3026561c13de0a4d3858d19d5793df180be90caea5bf19a2e59c1e4c572e79581f79ac76353b6d5cda557594; pt2gguin=o2644148694; uin=o2644148694; skey=M3DWO1AqLe; ptisp=cnc; ptcz=443da73108aac501c10660920c5aaa02540cad7113ee02c93c7f79830baf6fbf; webwx_auth_ticket=CIsBEI2J0OEHGoABObaMDAqLrZ9xodG09kK8PXWa7Wh2/tbfaH3SHMn+hZ+F+Rcq4PNWNI0P9Hb9zYwYLViRgLxIIjW99K0ZpGLSMJAknMIX4JlzpmU6xZvsThFhVg0peCdVhu4NY9qGayEDyjE77Yd2oZWPEA4VTVQBPpvEpVKaXDCaOive9UBseSo=; login_frequency=2; last_wxuin=1986578101; wxloadtime=1498715852_expired; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; wxpluginkey=1498697281; wxuin=1986578101; wxsid=897+WM8zp9J6mqar; webwx_data_ticket=gSfYm8bz+7MlcA1YDEnHQ0kk; mm_lang=en_US"
}

req = requests.get(url)

encoding = req.encoding

# print req.text.decode(encoding=encoding)

ss = u'''

'''.encode(encoding=encoding)

print ss