import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        if self.get_argument('u',None) in ['kevin','alvin']:
            # self.set_cookie('name',self.get_argument('u'))        #未加密cookie
            self.set_secure_cookie('user',self.get_argument('u'))   #加密cookie
        else:
            self.write('请登录')

class ManagerHandler(tornado.web.RequestHandler):

    def get(self):
        # if self.get_cookie('name',None) in ['kevin','alvin']:
        #     self.write('欢迎登陆' + self.get_cookie('name'))
        print(self.get_secure_cookie('user',None))
        if str(self.get_secure_cookie('user',None), encoding='utf-8') in ['kevin','alvin']:
            self.write('欢迎欢迎' + str(self.get_secure_cookie('user')))
        else:
            self.redirect('/index')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'cookie_secret': 'asdfasdfasdf',
}

application = tornado.web.Application([
    (r"/index",IndexHandler),
    (r"/manager",ManagerHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()