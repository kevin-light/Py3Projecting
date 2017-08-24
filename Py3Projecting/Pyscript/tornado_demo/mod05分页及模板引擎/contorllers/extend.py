import tornado.web
from core import Handler

class IndexHandler(Handler.MyHandler):
    def get(self,*args,**kwargs):
        print('456')
        self.render('extend/index.html',list_info=[1,2,3])

    def post(self,*args,**kwargs):
        pass

class FuckoffHandler(Handler.MyHandler):
    def get(self,*args,**kwargs):
        self.render('extend/fuck.html',list_info=[1,2,3])