import tornado.web
import tornado.ioloop

IMG_LIST = []
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',img_list=IMG_LIST)
    def post(self, *args, **kwargs):
        print(self.get_argument('user'))
        print(self.get_arguments('favor'))
        file_metas = self.request.files["fafafa"]
        for meta in file_metas:
            #要上传的文s件名
            file_name = meta['filename']
            import os
            with open(os.path.join('statics','img',file_name),'wb') as up:
                up.write(meta['body'])
            IMG_LIST.append(file_name)
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



