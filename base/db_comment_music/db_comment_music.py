from datetime import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class comment_music(base):
    __tablename__ = 'comment_music'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'))
    music = Column(Integer, ForeignKey('music.id'))
    comments = Column(String(2555), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="comment_music_realt")
    music_realt = relationship("music", uselist=False, back_populates="comment_music_realt")
