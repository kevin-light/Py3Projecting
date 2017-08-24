import pymysql
import tornado.ioloop
import tornado.web

class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('pwd',None)
        #创建数据库链接
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='db1')
        cursor = conn.cursor()

        # temp = "select * from user WHERE username='%s' and password='%s'" % (username,pwd,)
        # print(temp)    SQL注入,字符串格式化不行，

        #无法注入
        effect_row = cursor.execute("select * from user WHERE username='%s' and password='%s'" , (username,pwd,))
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if result:
            self.write('登录成功')
        else:
            self.write('登录失败')

settings = {
    'template_path': 'tpl',
    'static_path': 'statics',
    'static_url_prefix': '/sss/',
}

application = tornado.web.Application([
    (r"/login",LoginHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
