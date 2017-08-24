

# http://www.cnblogs.com/wupeiqi/articles/5713330.html
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker
print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/db1?charset=utf8",encoding="utf-8")
Base = declarative_base()  #生成一个sqlORM基类

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),index=True)
    fullname = Column(String(32),unique=True)
    password = Column(String(32))


    # __table_args__ = (
    # UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )           # 添加索引

    def __repr__(self):
        return "<User(name='%s',fullname='%s',password='%s')>" % (self.name,self.fullname,self.password)

def init_db():
    Base.metadata.create_all(engine)     #创建所有表结构

# def drop_db():
#     Base.metadata.drop_all(engine)
         #删除所有表结构

# ed_user = User(name='alvin',fullname='alvin king',password='111111')
# print(ed_user)

#这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
MySession = sessionmaker(bind=engine)
session = MySession()

# session.add(ed_user)
# our_user = session.query(User).filter_by(name='ed').first()
# = 查询 SELECT * from users where name='ed' limit 1;
# session.add_all([
#     User(name='kevin1',fullname='kevin jin1',password='123123'),
#     User(name='kevin2',fullname='kevin jin2',password='123123'),
#     User(name='kevin2',fullname='kevin jin3',password='123123'),
#
# ])
#
# session.commit()
#
# print('>>>',session.query(User).filter_by(name='kevin1').first())
# print(session.query(User).all())
# for row in session.query(User).order_by(User.id):
#     print(row)
# for row in session.query(User).filter(User.name.in_(['kevin1', 'wendy', 'jack'])):  #这里的名字是完全匹配
#     print(row)
# for row in session.query(User).filter(~User.name.in_(['kevin1', 'wendy', 'jack'])):   #这里的名字不匹配
#     print(row)
# print(session.query(User).filter(User.name == 'kevin1').count())                       #统计个数
from sqlalchemy import and_, or_

# for row in session.query(User).filter(and_(User.name == 'kevin1', User.fullname == 'kevin2')):
#     print(row)
for row in session.query(User).filter(or_(User.name == 'kevin1', User.name == 'kevin2')):
    print(row)



#
# # -*- coding:utf-8 -*-
# #coding:utf8
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# print(sqlalchemy.__version__)
#
#
# engine = create_engine('mysql+pymysql://root:111111@127.0.0.1:3306/db1?charset=utf8')
#
# Base = declarative_base()#生成一个SQLORM基类
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(40))
#     fullname = Column(String(40))
#     password = Column(String(40))
#
#     def __repr__(self):
#        return "<User(name='%s', fullname='%s', password='%s')>" % (
#                             self.name, self.fullname, self.password)
#
# Base.metadata.create_all(engine)  #创建所有表结构
#
# # ed_user = User(name='xiaoyu', fullname='Xiaoyu Liu', password='123')
# # print(ed_user)
# #这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
# MySession = sessionmaker(bind=engine)
# session = MySession()
# #
# # session.add(ed_user)
# our_user = session.query(User).filter_by(name='ed').first()
# # SELECT * FROM users WHERE name="ed" LIMIT 1;
# session.add_all([
#     User(name='alex', fullname='Alex Li', password='456'),
#     User(name='alex', fullname='Alex old', password='789'),
#     User(name='peiqi', fullname='Peiqi Wu', password='sxsxsx')])
#
# session.commit()

#print(">>>",session.query(User).filter_by(name='ed').first())
#print(session.query(User).all())
# for row in session.query(User).order_by(User.id):
#      print(row)
# for row in session.query(User).filter(User.name.in_(['alex', 'wendy', 'jack'])):＃这里的名字是完全匹配
#     print(row)
# for row in session.query(User).filter(~User.name.in_(['ed', 'wendy', 'jack'])):
#     print(row)
#print(session.query(User).filter(User.name == 'ed').count())
#from sqlalchemy import and_, or_

# for row in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
#     print(row)
# for row in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
#     print(row)