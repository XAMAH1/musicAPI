import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class history(base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), ForeignKey('user.nickname'))
    music = Column(Integer, ForeignKey('music.id'))
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="history_realt")
    music_realt = relationship("music", uselist=False, back_populates="history_realt")
