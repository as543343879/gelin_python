from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# class User(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# [
#     User('1', 'Michael'),
#     User('2', 'Bob'),
#     User('3', 'Adam')
# ]

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))



def addUser():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='5', name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def queryUser():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='5', name='Bob')
    # 添加到session:
    user = session.query(User).filter(User.id == '5').one()
    # user = session.query(User).filter(User.id == '5').one()
    # 提交即保存到数据库:
    # session.commit()
    # 关闭session:
    print("id={},name={}".format(user.id, user.name))
    session.close()


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/xxp')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# addUser()
queryUser()