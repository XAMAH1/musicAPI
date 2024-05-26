from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class device(base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    operation_system = Column(String(255), nullable=False)
    name_device = Column(String(255), nullable=False)
    ip_device = Column(String(255), nullable=False)
    version_program = Column(String(255), nullable=False)
    token_realt = relationship("token_autme", uselist=False, back_populates="device_realt")
