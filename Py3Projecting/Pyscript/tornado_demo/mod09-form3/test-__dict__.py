class MainForm(object):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
        self.port = "(\d+)"
        self.phone = "0?(13|14|15|18)[0-9]{9}"
# obj = MainForm()
# print(obj.__dict__)
    def check(self):
        for k , v in self.__dict__.items():
            print(k,v)
obj = MainForm()
obj.check()


# http://python.jobbole.com/83747/
# class Province:
#     country = 'China'
#
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def func(self, *args, **kwargs):
#         print('func')


# print(Province.__dict__)
#
# obj1 = Province('HeBei', 10000)
# print(obj1.__dict__)
#
# obj2 = Province('HeNan', 3888)
# print(obj2.__dict__)
