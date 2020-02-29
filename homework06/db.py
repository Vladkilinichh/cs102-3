from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scruputils import *


Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)

Base.metadata.create_all(bind=engine)

'''all = get_news('https://news.ycombinator.com/newest', 34)
s = session()
for new in all:
    news = News(title = new['title'],
                     author = new['author'],
                     url = new['urls'],
                     comments= new['comments'],
                     points = new['score'])
    s.add(news)
    s.commit()'''
