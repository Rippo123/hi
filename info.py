import re
from os import environ
from pyrogram import Client
from logging import WARNING, getLogger

getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Client
Bot = Client

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")


# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
BOT_USERNAME = "Phil_Coulson_Sflix_bot"
PREFIX = ["/", "!", "#", "!", "?", "^", "~"]
OWNER_ID = int(1617258761)
BOT_ID = int(2080723946)
