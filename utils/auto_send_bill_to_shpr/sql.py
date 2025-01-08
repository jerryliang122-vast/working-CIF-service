from sqlalchemy import create_engine, Column, Integer, String, TEXT, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class email_list(Base):
    _tablename_ = "email_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(TEXT)
    sender = Column(TEXT)
    receiver = Column(TEXT)
    date = Column(DateTime)


# 创建数据库
database = os.path.join(os.getcwd(), "conf", "auto_send_bill_to_shpr", "email_list.db")
engine = create_engine(f"sqlite:///{database}", echo=True)
Base.metadata.create_all(engine)
# 创建数据库连接
Session = sessionmaker(bind=engine)
