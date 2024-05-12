from .database import Base
from sqlalchemy import Column, String,Integer, TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email= Column(String, nullable=False)
    password = Column(String, nullable=False)
    created = Column(TIMESTAMP(timezone=True, server_default= text('now()')), nullable=False)
    