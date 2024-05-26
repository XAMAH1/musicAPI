from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class ban(base):
    __tablename__ = 'ban'

    id = Column(Integer, primary_key=True)
    rules = Column(String(255), nullable=False)
    time = Column(Time, nullable=False)
    description = Column(String(2555), nullable=True)
    ban_user_realt = relationship("ban_user", uselist=False, back_populates="ban_realt")
