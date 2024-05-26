from sqlalchemy.orm import relationship

from base.base import base
from sqlalchemy import *


class genre_music(base):
    __tablename__ = 'genre_music'

    id = Column(Integer, primary_key=True)
    genre = Column(Integer, ForeignKey("genre.id"))
    music = Column(Integer, ForeignKey("music.id"))
    genre_realt = relationship("genre", uselist=False, back_populates="genre_music_realt")
    music_realt = relationship("music", uselist=False, back_populates="genre_music_realt")
