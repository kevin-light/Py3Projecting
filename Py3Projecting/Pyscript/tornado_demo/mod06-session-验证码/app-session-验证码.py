import tornado.web
import tornado.ioloop

container = {}
# container = {
#     “第一个人的随机字符串”：{}，
#     ”第一个人的随机字符串“： {‘k1’：111，‘parents’：‘你’}，
# }

class Session:
    def __init__(self,handler):
        self.handler = handler
        self.random_str = None

    def __genarate_random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()),encoding='utf-8'))
        random_str = obj.hexdigest()
        return random_str

    def __setitem__(self, key, value):
        #在container中加入随机字符串，定义专属自己的数据，在客户端写入字符串，判断请求的用户是否有随机字符串
        if not self.random_str:
            random_str = self.handler.get_cookie('__kakaka__')
            if not random_str:
                random_str = self.__genarate_random_str()
                container[random_str] = {}
            else:
                #客户端有随机字符串
                if random_str in container.keys():
                    pass
                else:
                    random_str = self.__genarate_random_str()
                    container[random_str] = {}
            self.random_str = random_str

        container[self.random_str][key] = value
        self.handler.set_cookie("__kakaka__",self.random_str)

    def __getitem__(self,key):
        #获取客户端的随机字符串，从container中获取专属我的数据，专属信息[key]
        random_str = self.handler.get_cookie('__kakaka__')
        if not random_str:
            return None
        #客户端有随机字符串
        user_info_dict = container.get(random_str,None)
        if not user_info_dict:
            return None
        value = user_info_dict.get(key,None)
        return value

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)

class IndexHandler(BaseHandler):

    def get(self):
        if self.get_argument('u',None) in ['kevin','alvin']:
            # self.set_cookie('name',self.get_argument('u'))        #未加密cookie
            # self.set_secure_cookie('user',self.get_argument('u'))   #加密cookie
            self.session['is_login'] = True
            self.session['name'] = self.get_argument('u',None)
            print(container)
        else:
            self.write('请登录')

class ManagerHandler(BaseHandler):

    def get(self):
        # if self.get_cookie('name',None) in ['kevin','alvin']:
        #     self.write('欢迎登陆' + self.get_cookie('name'))
        # print(self.get_secure_cookie('user',None))
        # if str(self.get_secure_cookie('user',None), encoding='utf-8') in ['kevin','alvin']:
        #     self.write('欢迎欢迎' + str(self.get_secure_cookie('user')))
        val = self.session['is_login']
        if val:
            self.write(self.session['name'])
        else:
            self.redirect('/index')

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("login.html",status="")
    def post(self, *args, **kwargs):
        user = self.get_argument("user",None)
        pwd = self.get_argument('pwd',None)
        code = self.get_argument('code',None)
        check_code = self.session['CheckCode']
        if code.upper() == check_code.upper():
            self.write('验证码正确')
        else:
            self.render('login.html',status='验证码错误')

class CheckCodeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        #生成图片并返回
        import io
        import check_code
        mstream = io.BytesIO()
        #创建图片，并写入验证码
        img, code = check_code.create_validate_code()
        #将图片对象写入mstream
        img.save(mstream,"GIF")
        #为每个用户保存验证码
        self.session["CheckCode"] = code
        self.write(mstream.getvalue())


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'cookie_secret': 'asdfasdfasdf',
}

application = tornado.web.Application([
    (r"/index",IndexHandler),
    (r"/manager",ManagerHandler),
    (r"/login",LoginHandler),
    (r"/check_code",CheckCodeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()