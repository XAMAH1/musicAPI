import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class album_music(base):
    __tablename__ = 'album_music'

    id = Column(Integer, primary_key=True)
    music = Column(Integer, ForeignKey('music.id'), nullable=False)
    album = Column(Integer, ForeignKey('album.id'), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    album_realt = relationship("album", uselist=False, back_populates="album_music_realt")
    music_realt = relationship("music", uselist=False, back_populates="album_music_realt")
