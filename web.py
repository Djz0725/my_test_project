"""
@file: test_web
@author: DJZ
@time: 2020/12/14
@desc
"""

import tornado.web
import platform
import json

if platform.system() == "Windows":
    import asyncio

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class MainHander(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!")

    def post(self):
        data = self.request.body
        print(data)
        self.write("success!")
        self.finish()

class JSONObject:
  def __init__( self, dict ):
      vars(self).update( dict )

app = tornado.web.Application([
    ('/index',MainHander)
])



if __name__ == "__main__":
    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()