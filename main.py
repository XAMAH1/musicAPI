import datetime

from base.main import *

print('Успешно')

result = session.query(ban_user).filter(ban_user.mail == "cuperopen@mail.ru")


def test():
    mus = music()
    mus.path_music = 'test'
    mus.name = 'да'
    mus.duration = "15:00"
    mus.nickname = "XAMAH"
    session.add(mus)
    session.commit()


for i in result:
    print(i.autme_realt.user_realt.favourites_album_realt.album_realt.album_music_realt.music_realt.genre_music_realt.genre_realt.name)


result = session.query(genre_music).filter(genre_music.id == 1)

for i in result:
    print(i.music_realt.path_cover)
