'''
Description: 
Author: zhuohang li
Date: 2023-05-15 22:57:03
LastEditTime: 2023-05-15 23:02:37
LastEditors: zhuohang li
'''
from typing import Any, List, Optional, Type
from tornado.routing import _RuleList
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
from tornado.web import OutputTransform
define("port", type=int, default=10888)


class CustomAppication(tornado.web.Application):
    def __init__(self, handlers: _RuleList | None = None, default_host: str | None = None, transforms: List[Type[OutputTransform]] | None = None, **settings: Any) -> None:
        handlers = urls
        settings = configs
        super(CustomAppication, self).__init__(
            handlers, default_host, transforms, **settings)

def create_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomAppication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()