import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"CAACAgUAAxkBAAIHIWIe3hnLSbRnvB84m2jnJfh8jYwTAAI5BQACTH_xVF3UL5iKZjnsHgQ",
        caption=f"""""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥⚜️Powered By⚜️🔥", url=f"https://t.me/Attitude_Network")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "@Attitude_Network"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6e2ab05382cf91185b4fe.jpg",
        caption=f"""I M ALIVE......""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂𝗦𝘂𝗽𝗽𝗼𝗿𝘁🥂🔥", url=f"https://t.me/Oan_support")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["OAN_music", "Shaurya", "@Attitude_Network", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6e2ab05382cf91185b4fe.jpg",
        caption=f"""CLICK TO JOIN👇🏻""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂𝗖𝗵𝗮𝗻𝗻𝗲𝗹🥂🔥", url=f"Https://t.me/attitude_Network")
                ]
            ]
        ),
    )
