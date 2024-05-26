from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class genre(base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    genre_music_realt = relationship("genre_music", uselist=False, back_populates="genre_realt")
    preferences_genre_realt = relationship("preferences_genre", uselist=False, back_populates="genre_realt")
