"""
@file: test_web
@author: DJZ
@time: 2020/12/14
@desc
"""

import tornado.web

import platform

if platform.system() == "Windows":
    import asyncio

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class MainHander(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!")

    def post(self):
        self.write("hello world! post!")

app = tornado.web.Application([
    ('/index',MainHander)
])

if __name__ == "__main__":
    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()