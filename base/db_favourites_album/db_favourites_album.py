import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class favourites_album(base):
    __tablename__ = 'favourites_album'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'), nullable=False)
    album = Column(Integer, ForeignKey('album.id'), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="favourites_album_realt")
    album_realt = relationship("album", uselist=False, back_populates="favourites_album_realt")
