from sqlalchemy import *
from sqlalchemy import exc as sa_exc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import warnings

from base.base import base
from config import BASE_CONFIG

from base.db_subscription.db_subscription import *
from base.db_user.db_user import *
from base.db_role.db_role import *
from base.db_autme.db_autme import *
from base.db_token.db_token import *
from base.db_device.db_device import *
from base.db_ban.db_ban import *
from base.db_ban_user.db_ban_user import *
from base.db_music.db_music import *
from base.db_genre.db_genre import *
from base.db_genre_music.db_genre_music import *
from base.db_album.db_album import *
from base.db_album_music.db_album_music import *
from base.db_favourites_album.db_favourites_album import *
from base.db_comment_album.db_comment_album import *
from base.db_music_check.db_music_check import *
from base.db_history.db_history import *
from base.db_favourites_music.db_favourites_music import *
from base.db_music_ignore.db_music_ignore import *
from base.db_comment_music.db_comment_music import *
from base.db_preferences_genre.db_preferences_genre import *
from base.db_user_code.db_user_code import *

warnings.filterwarnings('ignore', category=sa_exc.SAWarning)


timeout = 10
engine = create_engine(f'mysql+pymysql://{BASE_CONFIG["BASE_USER"]}:{BASE_CONFIG["BASE_PASSWORD"]}@{BASE_CONFIG["BASE_HOST"]}/{BASE_CONFIG["BASE_TABLE"]}', connect_args={'connect_timeout': timeout})


base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
