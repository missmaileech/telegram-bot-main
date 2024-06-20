from operator import add
import os
import logging

from logging.handlers import RotatingFileHandler


TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7308876379:AAFb42hU7ul4j9vHVkofK84vBvlag00yB9k")
APP_ID = int(os.environ.get("APP_ID", "22518295"))
API_HASH = os.environ.get("API_HASH", "4ec4789e7af4207606a3d087923899f1")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002156410201"))
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/+3lKI_8wiXZ01ZDQ9")
OWNER_ID = int(os.environ.get("OWNER_ID", "1077671360"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sachinanand9990558619:ugBEd1iVU0VJAAcP@cluster0.9uhmlry.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "missmai0")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
OWNER_TAG = "Savoryrabbit"
ADMINS = [5695568361, 7179528076, 5618890876, 6773748306, 860596271]
TIME = int(os.environ.get("TIME", "60"))

try:
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"
ADMINS.append(OWNER_ID)     

#Shortner (token system) 

#Keep this true if you want to use this feature otherwise False.
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "False") == "True" else False 
#Shortlink url there are many <<share the urls to them
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "droplink.co/api")
#shortlink url api key
SHORTLINK_API = os.environ.get("SHORTLINK_API", "93b387211406580301f396a05797fe59ba95ad42")
#leave it as it is. used as a timer in seconds untill the user can verify.
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400))
#
#Tutorial Video uploaded somewhere in your channel link
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_Download_7x/32")


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
