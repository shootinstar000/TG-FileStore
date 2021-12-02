# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "2557747"))
	API_HASH = os.environ.get("API_HASH", "3022e575059ce68696f4fa4120ae33a2")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "2122160445:AAENV5wX9Eei3nACUGYmzMeSPJ2YSY-wr_w")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "bratflix_storage_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001437481802"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "879778871"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://lilbrat:lilbrat@cluster0.c9kkp.mongodb.net/myFirstDatabase?retryWrites=true")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001423915127")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001437481802")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
This is a private bot only for @bratflix 
╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [Bratflix storage 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)
│
├🔸👨‍💻 **owner:** [@lilbratsagar](https://t.me/lilbratsagar) 
│
├🔸🔔 **Backup :** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/bratflix)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Owner:** [@lilbratsagar](https://t.me/lilbratsagar) 

"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot** For @bratflix.

This Bot is not for public us, so u can't use it to store movies

⚠️ If u see 👉  _PART_0001 or _PART_0002 👈 at the end of file name then avoid downloading that movie bcz u have to download all the parts in order to watch the full movie or episode

"""
