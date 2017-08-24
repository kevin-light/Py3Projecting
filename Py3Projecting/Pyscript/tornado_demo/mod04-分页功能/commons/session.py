import tornado.web

from contorllers import home

settings = {
    'template_path': 'views', #模板路径的配置
    'static_path':'statics',

}

#路由映射，路由系统
application = tornado.web.Application([
    # (r"/index/(?P<num>\d*)/(?P<nid>\d*)",home.IndexHandler),
    (r"/index/(?P<page>\d*)", home.IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()