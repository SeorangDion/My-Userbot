import os, sys
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = os.environ.get("API_ID", 6)
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
STRING_SESSION = os.environ.get("STRING_SESSION", None)

if not STRING_SESSION:
    print("[ERROR]: SESSION_STRING does not exist. Please enter SESSION_STRING! Userbot out.")
    sys.exit(1)

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
