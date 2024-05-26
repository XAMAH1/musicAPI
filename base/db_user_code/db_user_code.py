import datetime

from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class user_code(base):
    __tablename__ = 'user_code'

    id = Column(Integer, primary_key=True)
    mail = Column(String(255), ForeignKey('user.mail'))
    code = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    date_create = Column(DateTime, nullable=False, default=datetime.datetime.today())
    time = Column(Time, nullable=False, default=datetime.datetime.today())
    date_use = Column(DateTime, nullable=True, default=datetime.datetime.today())
    isUse = Column(Boolean, nullable=False, default=False)

    user_realt = relationship("user", uselist=False, back_populates="user_code_realt")
