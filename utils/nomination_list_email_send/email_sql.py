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
database = os.path.join(os.getcwd(), "conf", "agent_email_nomination_list.db")
engine = create_engine(f"sqlite:///{database}", echo=True)
Base.metadata.create_all(engine)
# 创建数据库连接
Session = sessionmaker(bind=engine)
