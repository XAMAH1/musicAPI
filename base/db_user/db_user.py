from datetime import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class user(base):
    __tablename__ = 'user'

    nickname = Column(String(255), primary_key=True)
    FIO = Column(String(255), nullable=False)
    mail = Column(String(255), ForeignKey('autme.mail'))
    picture_path = Column(String(2555), nullable=False, default="picture/static/user.png")
    birthday = Column(DateTime, nullable=False)
    phone = Column(String(20), nullable=True)
    subscription = Column(Integer, ForeignKey('subscription.id'))
    date_subscription = Column(DateTime, nullable=True, default=datetime.today())
    isHide = Column(Boolean, nullable=False, default=False)
    isRemove = Column(Boolean, nullable=False, default=False)

    autme_realt = relationship("autme", uselist=False, back_populates="user_realt")
    subscription_realt = relationship("subscription", uselist=False, back_populates="user_realt")
    music_realt = relationship("music", uselist=False, back_populates="user_realt")
    album_realt = relationship("album", uselist=False, back_populates="user_realt")
    favourites_album_realt = relationship("favourites_album", uselist=False, back_populates="user_realt")
    favourites_music_realt = relationship("favourites_music", uselist=False, back_populates="user_realt")
    music_ignore_realt = relationship("music_ignore", uselist=False, back_populates="user_realt")
    comment_album_realt = relationship("comment_album", uselist=False, back_populates="user_realt")
    comment_music_realt = relationship("comment_music", uselist=False, back_populates="user_realt")
    music_check_realt = relationship("music_check", uselist=False, back_populates="user_realt")
    history_realt = relationship("history", uselist=False, back_populates="user_realt")
    preferences_genre_realt = relationship("preferences_genre", uselist=False, back_populates="user_realt")
    user_code_realt = relationship("user_code", uselist=False, back_populates="user_realt")
