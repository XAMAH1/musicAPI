import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class music_check(base):
    __tablename__ = 'music_check'

    music = Column(Integer, ForeignKey('music.id'), primary_key=True)
    admin_user = Column(String(255), ForeignKey('user.nickname'))
    isCheck = Column(Boolean, nullable=False, default=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())

    user_realt = relationship("user", uselist=False, back_populates="music_check_realt")
    music_realt = relationship("music", uselist=False, back_populates="music_check_realt")
