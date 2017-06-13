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

from datetime import datetime

from elasticsearch import Elasticsearch

# 连接elasticsearch, 默认9200
es = Elasticsearch()

doc = {
    'author': 'jicius',
    'text': 'Es',
    'timestamp': datetime.now()
}
# 创建索引, 如果索引存在, 返回400
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['created'])

# get方式取数据
res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

# search方式取数据
res = es.search(index="test-index", body={"query": {"march_al": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])