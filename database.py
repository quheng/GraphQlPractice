# coding=utf8
# Author: quheng

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from config import DATABASE_ADDR
from config import DATABASE_USER
from config import DATABASE_PWD

_engine = 'mysql://'
_engine += DATABASE_USER + ':'
_engine += DATABASE_PWD + '@'
_engine += DATABASE_ADDR + ':3306/'
_engine += "crunchbase"
# print _engine
_engine = create_engine(_engine)
DBSession = sessionmaker(bind=_engine)

def test():
    session = DBSession()
