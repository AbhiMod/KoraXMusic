import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","2027757649:AAEXHXne2pykl5PYa_12M1HiCsXE7PvTVnI")
BOT_USERNAME = getenv("BOT_USERNAME" , "Kora_Xbot")
ASSUSERNAME = getenv("ASSUSERNAME" , "KoraMusicAssist")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://korabot:Kushal@cluster0.pjrfx.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999999"))
LOGGER_ID = int(getenv("LOGGER_ID",-1001840241140))
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/KoraXMusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/b7abd692eacb5ca13737e.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/b7abd692eacb5ca13737e.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
STATS_IMG_URL = "https://graph.org/file/b7abd692eacb5ca13737e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b7abd692eacb5ca13737e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/e7a8c2b902d3e2fefd4ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
