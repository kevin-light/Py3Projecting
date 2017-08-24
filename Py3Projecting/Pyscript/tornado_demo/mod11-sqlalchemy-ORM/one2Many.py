from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/db1",echo=True)
Base = declarative_base()

Base = declarative_base()

class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))

    father_id = Column(Integer, ForeignKey('father.id'))
    # father = relationship('Father')
    #
    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )


class Father(Base):
    __tablename__ = 'father'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    son = relationship('Son',backref='father')       #查询关系字段,backref代替Son下面的 father = relationship('Father')



def init_db():
    Base.metadata.create_all(engine)     #创建所有表结构

# def drop_db():
#     Base.metadata.drop_all(engine)
         #删除所有表结构

Session = sessionmaker(bind=engine)
session = Session()

# f1 = Father(name='alvin', age=50)
# w1 = Son(name='little alvin1', age=4,father_id=1)
# w2 = Son(name='little alvin2', age=5,father_id=1)
#
# # f1.son = [w1, w2]
#
# session.add_all([f1,w1,w2])
# session.commit()

# ret=session.query(Father.name,Son.id).join(Son).all()   #普通查询
# print(ret)
# ret=session.query(Father).filter_by(id=1).all()     #all()取到的是对象
# print(ret)

f1=session.query(Father).filter_by(id=1).first()        # 有relationship可以跨表查询
print(f1.son)
for i in f1.son:
    print(i.name)

f1=session.query(Son).filter_by(id=2).first()        # 有relationship可以跨表查询
print(f1.father.name,f1.name)
