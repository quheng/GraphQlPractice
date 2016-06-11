# coding=utf8
# Author: quheng

from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from config import DATABASE_ADDR
from config import DATABASE_USER
from config import DATABASE_PWD

# creat engine and session
_engine = 'mysql://'
_engine += DATABASE_USER + ':'
_engine += DATABASE_PWD + '@'
_engine += DATABASE_ADDR + ':3306/'
_engine += "crunchbase"
_engine = create_engine(_engine)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=_engine))


# reflect table
_Base = automap_base()
_Base.prepare(_engine, reflect=True)

Acquisitions = _Base.classes.cb_acquisitions
Degrees = _Base.classes.cb_degrees
FundingRounds = _Base.classes.cb_funding_rounds
Funds = _Base.classes.cb_funds
Investments = _Base.classes.cb_investments
Ipos = _Base.classes.cb_ipos
Milesones = _Base.classes.cb_milestones
Objects = _Base.classes.cb_objects
Offices = _Base.classes.cb_offices
People = _Base.classes.cb_people
Relationships = _Base.classes.cb_relationships

def test():
    """
    test database connection
    """
    res = "http://blog.seattlepi.nwsource.com/venture/archives/118242.asp"
    return session.query(Acquisitions).filter(Acquisitions.id == '5').one().source_url == res
