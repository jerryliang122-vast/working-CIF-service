from sqlalchemy import create_engine, Column, Integer, String, TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class Agent(Base):
    __tablename__ = "agent_email_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    port = Column(TEXT)
    name = Column(TEXT)
    email = Column(TEXT)


# 创建数据库
database = os.path.join(os.getcwd(), "conf", "agent_email.db")
engine = create_engine("sqlite:///{}".format(database), echo=True)
Base.metadata.create_all(engine)


# 创建一个seession 类
class Session(object):
    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = sessionmaker(bind=engine)()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    # 插入数据
    def insert(self, name, email):
        with self as session:
            agent = Agent(name=name, email=email)
            session.add(agent)

    # 读取代理名字
    def read_name(self):
        with self as session:
            data = session.query(Agent.name).all()
            # 将元组转换成列表
            data = [i[0] for i in data]
            return data

    # 读取代理邮箱
    def read_email(self, name):
        with self as session:
            data = session.query(Agent.email).filter(Agent.name == name).first()
            return data[0]

    # 按照港口读取代理名称列表
    def read_port_name(self, port):
        with self as session:
            data = session.query(Agent.name).filter(Agent.port.like("%{}%".format(port))).all()
            data = [i[0] for i in data]
            return data
