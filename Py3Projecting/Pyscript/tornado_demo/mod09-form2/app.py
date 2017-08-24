import tornado.ioloop
import tornado.web
import re,os

class IPFiled:

    REGULAR = "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"

    def __init__(self,error_dict=None,required=True):
        #封装错误信息，error_dict自定义错误
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None
        self.value = None
        self.is_valid = False

    def validate(self,name,input_value):
        '''
        :param name: 字段名
        :param input_value:用户表单输入的内容
        :return:
        '''
        if not self.required:
            #用户输入可以为空
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value.strip():
                if self.error_dict.get('required',None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                ret = re.match(IPFiled.REGULAR,input_value)
                if ret:
                    self.is_valid = True
                    self.value = input_value
                else:
                    if self.error_dict.get('valid',None):
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name

class StringFiled:

    REGULAR = "^(.*)$"

    def __init__(self,error_dict=None,required=True):
        #封装错误信息，error_dict自定义错误
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None
        self.value = None
        self.is_valid = False

    def validate(self,name,input_value):
        '''
        :param name: 字段名
        :param input_value:用户表单输入的内容
        :return:
        '''
        if not self.required:
            #用户输入可以为空
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value.strip():
                if self.error_dict.get('required',None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                ret = re.match(IPFiled.REGULAR,input_value)
                if ret:
                    self.is_valid = True
                    self.value = input_value
                else:
                    if self.error_dict.get('valid',None):
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name

class ChechBoxFiled:

    def __init__(self,error_dict=None,required=True):
        #封装错误信息，error_dict自定义错误
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)

        self.required = required
        self.error = None
        self.value = None
        self.is_valid = False

    def validate(self,name,input_value):
        '''
        :param name: 字段名
        :param input_value:用户表单输入的内容
        '''
        if not self.required:
            #用户输入可以为空
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value:
                if self.error_dict.get('required',None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                self.is_valid = True
                self.value = input_value

class FileFiled:

    REGULAR = "^(\w+\.pdf)|(\w+\.mp3)|(\w+\.py)$"

    def __init__(self,error_dict=None,required=True):
        #封装错误信息，error_dict自定义错误
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required

        self.error = None
        self.value = []
        self.is_valid = True
        self.name = None
        self.success_file_name_list = []

    def validate(self,name,all_file_name_list):
        '''
        :param name: 字段名
        :param all_file_name_list:所有文件文件名
        :return:
        '''
        self.name = name
        if not self.required:
            #用户输入可以为空
            self.is_valid = True
            self.value = all_file_name_list
        else:
            if not all_file_name_list:
                self.is_valid = False
                if self.error_dict.get('required',None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                #循环所有文件名
                for file_name in all_file_name_list:
                    ret = re.match(FileFiled.REGULAR,file_name)
                    if not ret:
                        self.is_valid = False
                        if self.error_dict.get('valid',None):
                            self.error = self.error_dict['valid']
                        else:
                            self.error = "%s is invalid" % name
                        break
                else:
                    self.value.append(file_name)

    def save(self,request,path='statics'):

        #所有文件列表
        temp_list = []
        file_metas = request.files.get(self.name)
        # 循环文件列表
        for meta in file_metas:
            #每个文件文件名
            file_name = meta['filename']
            #设置保存文件路径
            new_file_name = os.path.join(path,file_name)

            if file_name and file_name in self.value:
                temp_list.append(new_file_name)
                with open(new_file_name,'wb') as up:
                    up.write(meta['body'])
        self.value = temp_list


class BaseForm:
    def check_valid(self, handle):
        flag = True
        error_massage_dict = {}
        success_value_dict = {}
        for key, regular in self.__dict__.items():
                #key: ip... ,
                # handle: homeIndex对象，self.get
                #regular: IPFiled(required=True）
            if type(regular) == ChechBoxFiled:
                input_value = handle.get_arguments(key)
            elif type(regular) == FileFiled:
                #获取文件名
                file_list = handle.request.files.get(key)
                input_value = []
                for item in file_list:
                    input_value.append(item['filename'])
            else:
                input_value = handle.get_argument(key)

            #input_value = 用户输入的值
            regular.validate(key,input_value)

            if regular.is_valid:
                success_value_dict[key] = regular.value
            else:
                error_massage_dict[key] = regular.error
                flag = False

        return flag, success_value_dict, error_massage_dict


class IndexForm(BaseForm):
    def __init__(self):
        self.host = "(.*)"
        # self.ip = IPFiled(required=False)
        self.ip = "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
        self.port = "(\d+)"
        self.phone = "0?(13|14|15|18)[0-9]{9}"


class HomeForm(BaseForm):
    def __init__(self):
        self.ip = IPFiled(required=True,error_dict={'required':'别整空的','valid':'骚年，格式错误'})
        self.host = StringFiled(required=False)
        self.favor = ChechBoxFiled(required=True)
        self.fafafa = FileFiled(required=True)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html',error_dict=None)

    def post(self, *args, **kwargs):

        # files = self.request.files.get('fafafa',[])
        # print(type(files),files)

        obj = HomeForm()
        # 获取用户输入的内容，和正则表达式匹配
        is_valid, success_dict,error_dict = obj.check_valid(self)
        # print(is_valid)
        # 如果全部验证成功，将输入的数据放置obj.value_dict
        if is_valid:
            print("success",success_dict)
            obj.fafafa.save(self.request)
        else:
            print('error',error_dict)
            self.render('home.html',error_dict=error_dict)


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
}
application = tornado.web.Application([
    # (r"/index",IndexHandler),
    (r"/home",HomeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()