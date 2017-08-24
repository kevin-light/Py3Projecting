# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/db1?charset=utf8",max_overflow=5)

Base = declarative_base()

class Men_to_Women(Base):
    __tablename__ = "men_to_women"
    id = Column(Integer,primary_key=True)
    men_id = Column(Integer,ForeignKey("men.id"))
    women_id = Column(Integer,ForeignKey("women.id"))

class Men(Base):
    __tablename__ = "men"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    age = Column(String(32))
    # gf = relationship("Women", secondary=Men_to_Women.__table__)

class Women(Base):
    __tablename__ = "women"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    age = Column(String(32))
    bf = relationship("Men",secondary=Men_to_Women.__table__,backref='gf')

def init_db():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# m1 = Men(name='alvin',age=18)
# m2 = Men(name='kevin',age=16)
# w1 = Women(name='honghong',age=16)
# w2 = Women(name='huahua',age=16)
# t1 = Men_to_Women(men_id=1,women_id=2)

f1 = session.query(Men).filter_by(id=1).first()
f2 = session.query(Women).all()
f1.gf = f2
session.add_all([f1,])
session.commit()