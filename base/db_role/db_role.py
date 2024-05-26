from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class role(base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    autme_realt = relationship("autme", uselist=False, back_populates="role_realt")
