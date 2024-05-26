from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class subscription(base):
    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Double, nullable=False)
    description = Column(String(2555), nullable=False, default="Отсутствует")
    user_realt = relationship("user", uselist=False, back_populates="subscription_realt")
