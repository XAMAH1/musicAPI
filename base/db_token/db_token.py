from datetime import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class token_autme(base):
    __tablename__ = 'token_autme'

    token = Column(String(528), primary_key=True)
    mail = Column(String(255), ForeignKey('autme.mail'))
    date = Column(DateTime, nullable=False, default=datetime.today())
    device = Column(Integer, ForeignKey('device.id'))
    autme_realt = relationship("autme", uselist=False, back_populates="token_realt")
    device_realt = relationship("device", uselist=False, back_populates="token_realt")
