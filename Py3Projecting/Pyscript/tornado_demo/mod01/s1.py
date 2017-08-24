import tornado.ioloop
import tornado.web
import uimethod as mt
import uimodule as md

INPUTS_LIST = []
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("hello world")
        # self.render("s1.html")
        name = self.get_argument('xxx',None)
        if name:
            INPUTS_LIST.append(name)
        self.render("s1.html",npm="NPM888", xxxooo=INPUTS_LIST)
    def post(self, *args, **kwargs):

        name = self.get_argument('xxx',None)
        print(name)
        INPUTS_LIST.append(name)
        self.render("s1.html",xxxooo=INPUTS_LIST)
        # self.write("hello world")

settings = {
    'template_path': 'tpl',  #模板路径的配置
    'static_path': 'static',
    'static_url_prefix': '/sss/',
    'ui_method': 'mt',
    'ui_module': 'md',
}

#路由映射，路由系统
application = tornado.web.Application([
    (r"/index",MainHandler),

], **settings)

if __name__ == '__main__':
    # socket运行起来
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()