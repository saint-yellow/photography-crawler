from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine('mysql+pymysql://root:saint-yellow@localhost:3306/beauty_photography')

Base = declarative_base()


class PhotoCollection(Base):
    __tablename__ = 'photo_collections'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), nullable=True)
    author = Column(String(1024), nullable=True)
    source = Column(String(1024), nullable=True)
    url = Column(String(1024), nullable=True)
    datetime_published = Column(DateTime(), nullable=True)
    description = Column(String(1024), nullable=True)
    tags = Column(String(1024), nullable=True)
    datetime_crawled = Column(DateTime(), default=datetime.now)

    def __init__(self, url, title, source, author, datetime_published, description, tags):
        self.url = url
        self.title = title
        self.source = source
        self.author = author
        self.datetime_published = datetime_published
        self.description = description
        self.tags = self.tags


class PhotoDetail(Base):
    __tablename__ = 'photo_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), nullable=True)
    webpage_url = Column(String(1024), nullable=True)
    photo_url = Column(String(1024), nullable=True)
    datetime_crawled = Column(DateTime(), default=datetime.now)

    def __init__(self, title, webpage_url, photo_url):
        self.title = title
        self.webpage_url = webpage_url
        self.photo_url = photo_url

        

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)