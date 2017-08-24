from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/db1?charset=utf8")
Base = declarative_base()

class HostToGroup(Base):
    __tablename__ = 'host_2_group'
    nid = Column(Integer,primary_key=True,)
    host_id = Column(Integer,ForeignKey('host.id'))
    group_id = Column(Integer,ForeignKey('group.id'))

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(32),unique=True,nullable=False)
    ip_addr = Column(String(32),unique=True,nullable=False)
    port = Column(Integer,default=22)
    group = relationship("Group",secondary=HostToGroup.__table__,backref='host_list')
    def __repr__(self):
        return  "<id=%s,hostname=%s, ip_addr=%s>" %(self.id,
                                                    self.hostname,
                                                    self.ip_addr)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),unique=True,nullable=False)

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id,self.name)


Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    #
    # g1 = Group(name='g1')
    # g2 = Group(name='g2')
    # g3 = Group(name='g3')
    #
    # h1 = Host(hostname='h1',ip_addr='1.0.0.9')
    # h2 = Host(hostname='h2',ip_addr='1.0.0.8',port=1111)
    # h3 = Host(hostname='h3',ip_addr='1.0.0.3',port=1113)
    #
    # session.add_all([g1,g2,g3,h1,h2,h3])
    # session.commit()

    groups = session.query(Group).all()                             # all得到对象
    h2 = session.query(Host).filter(Host.hostname=='h2').first()     # first得到列表
    h2.group = groups[:-1]
    print('+++++>',h2.group)

    g3 = session.query(Group).filter(Group.name=='g3').first()
    print(g3)
    obj1 = session.query(Host).filter(Host.hostname=='h1').update({'port':333})
    obj2 = session.query(Host).filter(Host.hostname=='h1').first()
    print("h1:",obj2.group)
    print('g:',g3.host_list)

    g3.host_list=[obj2,]
    # obj2.group=[g3,]

    session.commit()