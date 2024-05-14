from .database import Base
from sqlalchemy import Column, String,Integer, TIMESTAMP, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email= Column(String, nullable=False)
    password = Column(String, nullable=False)
    created = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    
class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content =Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('userS.id', ondelete='CASCADE'), nullable=False)

    owner = relationship('User')