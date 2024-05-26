import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class album(base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    nickname = Column(String(255), ForeignKey('user.nickname'), nullable=False)
    count_music = Column(Integer, nullable=False, default=0)
    description = Column(String(2555), nullable=True)
    cover_album_path = Column(String(2555), nullable=False, default="picture/static/cover.png")
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="album_realt")
    album_music_realt = relationship("album_music", uselist=False, back_populates="album_realt")
    favourites_album_realt = relationship("favourites_album", uselist=False, back_populates="album_realt")
    comment_album_realt = relationship("comment_album", uselist=False, back_populates="album_realt")
