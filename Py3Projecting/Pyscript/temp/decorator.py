# # 无参装饰器,有参函数
# def wrapper(func):
#     def inner(name1):  # 这个参数最终会传给这个函数体内部需要调用参数的对象
#         func(name1)  # 这个参数个数是由原来的函数,也就是我们这里的index函数决定参数个数的
#     return inner
#
#
# @wrapper  # 使用装饰器
# def index(name):  # 传入一个参数
#     print('welcome %s' % name)
#
# index('zengchunyun')

# 无参装饰器,多参函数
# def wrapper(func):
#     def inner(*args):  # 使用动态参数
#         func(*args)
#     return inner
#
#
# @wrapper  # 使用装饰器
# def index(*args):  # 传入一个参数
#     print('welcome %s' % '   '.join(args))
#
# index('zengchunyun', 'goodbye')

import shutil
import os

# asd = open("test",'w')


import copy

n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}

n3 = copy.copy(n1)
n4 = copy.deepcopy(n1)
print(n3,n4)