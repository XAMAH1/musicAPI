import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class preferences_genre(base):
    __tablename__ = 'preferences_genre'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'), nullable=False)
    genre = Column(Integer, ForeignKey('genre.id'), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="preferences_genre_realt")
    genre_realt = relationship("genre", uselist=False, back_populates="preferences_genre_realt")
