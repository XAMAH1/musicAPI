from datetime import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class autme(base):
    __tablename__ = 'autme'

    mail = Column(String(255), primary_key=True)
    password = Column(String(255), nullable=False)
    role = Column(Integer, ForeignKey('role.id'))
    date_create = Column(DateTime, nullable=False, default=datetime.today())
    role_realt = relationship("role", uselist=False, back_populates="autme_realt")
    user_realt = relationship("user", uselist=False, back_populates="autme_realt")
    token_realt = relationship("token_autme", uselist=False, back_populates="autme_realt")
    ban_realt = relationship("ban_user", uselist=False, back_populates="autme_realt")
