import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Torrent-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.safone.tech/torrent?query="

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply(
        text="Hello I'am a simple Torrent finder Bot."
    )


@Bot.on_message(filters.private & filters.text)
async def reply_info(bot, message):
    await message.reply(
        text=torrent(message.text)
    )


def torrent(query):
    try:
        r = requests.get(API + requote_uri(query.lower()))
        info = r.json()
        name = info['name']
        category = info['category']
        description = info['description']
        genre = info['genre']
        infoHash = info['infoHash']
        language = info['language']
        lastChecked = info['lastChecked']
        seeders = info['seeders']
        leechers = info['leechers']
        size = info['size']
        uploaderLink = info['uploaderLink']
        uploadDate = info['uploadDate']
        magnetLink = magnetLink['longitude']
        torrent = f"""--**Torrent Information**--

Name : `{name}`
Category : `{category}`
Description : `{description}`
Genre : `{genre}`
Info HASH : `{infoHash}`
Language : `{language}`
Size : `{size}`
Last Checked : `{lastChecked}`
Seeders : `{seeders}`
Leechers : `{leechers}`
Uploader Link : `{uploaderLink}`
Upload Date : `{uploadDate}`
Magnet Link : `{magnetLink}`"""
        return torrent
    except Exception as error:
        return error


Bot.run()
