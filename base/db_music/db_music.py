import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class music(base):
    __tablename__ = 'music'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    path_music = Column(String(2555), nullable=False)
    path_cover = Column(String(2555), nullable=False, default="picture/static/cover.png")
    duration = Column(Time, nullable=False)
    isCheck = Column(Boolean, nullable=False, default=False)
   # isHide = Column(Boolean, nullable=False, default=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())
    nickname = Column(String(255), ForeignKey('user.nickname'),  nullable=False)

    user_realt = relationship("user", uselist=False, back_populates="music_realt")
    genre_music_realt = relationship("genre_music", uselist=False, back_populates="music_realt")
    album_music_realt = relationship("album_music", uselist=False, back_populates="music_realt")
    music_check_realt = relationship("music_check", uselist=False, back_populates="music_realt")
    history_realt = relationship("history", uselist=False, back_populates="music_realt")
    favourites_music_realt = relationship("favourites_music", uselist=False, back_populates="music_realt")
    music_ignore_realt = relationship("music_ignore", uselist=False, back_populates="music_realt")
    comment_music_realt = relationship("comment_music", uselist=False, back_populates="music_realt")

