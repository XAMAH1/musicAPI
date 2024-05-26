from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class ban_user(base):
    __tablename__ = 'ban_user'

    id = Column(Integer, primary_key=True)
    mail = Column(String(255), ForeignKey('autme.mail'))
    reason_ban = Column(Integer, ForeignKey('ban.id'))
    date_ban = Column(DateTime, nullable=False)
    autme_realt = relationship("autme", uselist=False, back_populates="ban_realt")
    ban_realt = relationship("ban", uselist=False, back_populates="ban_user_realt")
