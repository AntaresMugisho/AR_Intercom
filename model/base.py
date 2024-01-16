# -*- This python file uses the following encoding : utf-8 -*-


from datetime import datetime

from sqlalchemy import create_engine, event, Engine, Column, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from utils import STORAGE_DIR


engine = create_engine(f"sqlite:///{STORAGE_DIR}/db.db", echo=False)

db = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine)
)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Model = declarative_base()
Model.query = db.query_property()


class TimeStampedModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())

    def update(self):
        self.updated_at = datetime.utcnow()