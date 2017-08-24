import tornado.ioloop
import tornado.web
import re


class MainForm(object):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
        self.port = "(\d+)"
        self.phone = "0?(13|14|15|18)[0-9]{9}"

    def check_valid(self, handler):
        flag = True
        value_dict = {}
        for key, regular in self.__dict__.items():
            input_value = handler.get_argument(key)
            val = re.match(regular, input_value)
            print(key, input_value, val, regular)
            if not val:
                flag = False
            value_dict[key] = input_value
        return flag, value_dict


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = MainForm()
        # 获取用户输入的内容，和正则表达式匹配
        is_valid, value_dict = obj.check_valid(self)
        print(is_valid)
        # 如果全部验证成功，将输入的数据放置obj.value_dict
        if is_valid:
            print(value_dict)


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
}
application = tornado.web.Application([
    (r"/index",IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()