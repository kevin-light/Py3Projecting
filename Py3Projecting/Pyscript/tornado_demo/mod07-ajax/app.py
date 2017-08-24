import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self, *args, **kwargs):
        print(self.get_argument('k1'))
        self.write('{"status":1,"message":"mmm"}')

settings = {
    'template_path': 'views', #模板路径的配置
    'static_path':'statics',
    'static_url_prefix': '/statics/',

}

#路由映射，路由系统
application = tornado.web.Application([
    (r"/index",IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



