from datetime import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class comment_album(base):
    __tablename__ = 'comment_album'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'))
    album = Column(Integer, ForeignKey('album.id'))
    comments = Column(String(2555), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="comment_album_realt")
    album_realt = relationship("album", uselist=False, back_populates="comment_album_realt")
