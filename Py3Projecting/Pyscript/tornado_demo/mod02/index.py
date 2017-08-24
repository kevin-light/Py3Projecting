import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        co = self.get_cookie('auth')
        if co == '1':
            self.render('manager.html')
        else:
            self.render('/loggin')
class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth','0')
        self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text="")
    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        if username == 'alex' and pwd == 'sb':
            self.set_cookie('auth','1')
            self.redirect('/manager')
        else:
            self.render('login.html',status_text="登录失败")

settings = {
    'template_path':'views',    #配置模板路径

}

application = tornado.web.Application([
    (r"/index",IndexHandler),
    (r"/login",LoginHandler),
    (r"/manager",ManagerHandler),
    (r"/logout",LogoutHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()