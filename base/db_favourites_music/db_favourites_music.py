import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class favourites_music(base):
    __tablename__ = 'favourites_music'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'), nullable=False)
    music = Column(Integer, ForeignKey('music.id'), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="favourites_music_realt")
    music_realt = relationship("music", uselist=False, back_populates="favourites_music_realt")
