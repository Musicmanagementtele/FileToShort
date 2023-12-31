# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '13415474'))
    API_HASH = str(getenv('API_HASH', '01bb828c0429beeabd6e9e841d026231'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6434399232:AAFy94DNlPbOjzQlrMEoKcwjeHWRnJGmxFI'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'File-To-Link'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001848305113'))
    PORT = int(getenv('PORT', 8080))
    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "BOTTOM")
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1471469091").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    SHORTENER_API = str(getenv('SHORTENER_API', '02c93c55c4567035a37ffc32731d8f0e1c530f98'))
    SHORTENER_WEBSITE = str(getenv('SHORTENER_WEBSITE', 'tnshort.net'))
    FDQN = str(getenv('FDQN', ''))

    APP_NAME = None
    OWNER_USERNAME = str(getenv('thavarajtj'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', ''))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://hillsking1222:kuraman1@kumaran1.d6ahc05.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "SAM_DUB_LEZHa"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
