# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent

from fake_proxy.config import config

ua = UserAgent()
config = config.get('default')


class AgentMiddleware(object):
    """ UserAgent 代理"""
    def process_request(self, request, spider):
        request.headers.Headers = config.headers
        request.headers['User-Agent'] = ua.random