# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/testdb", max_overflow=5)

Base = declarative_base()

# 创建单表
class Users(Base):
    __tablename__ = 'usertest2'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

def init_db():
    Base.metadata.create_all(engine)

# def drop_db():
#     Base.metadata.drop_all(engine)
x = (b"\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA").decode()
print(x)

#的空间奥斯卡的将来

#from pymysql import cursors