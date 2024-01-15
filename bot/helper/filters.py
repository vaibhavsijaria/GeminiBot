from pyrogram import filters
from pyrogram.types import Message, InlineQuery

from bot.config import sudo_usr, auth_chats

async def sudo_check(_, __, msg: Message):
    """Check if the message is from a sudo user."""
    return msg.from_user.id in sudo_usr if msg.from_user else False

async def auth_check(_, __, msg: Message):
    """Check if the message is from an authorized chat."""
    return msg.chat.id in auth_chats

async def gemini_img(_, __, msg: Message):
    """Check if the message is a photo with a caption starting with '/ask' or a text message replying to a photo with '/ask'."""
    return (msg.photo and msg.caption and msg.caption.startswith('/ask')) or (msg.text and msg.text.startswith('/ask') and msg.reply_to_message and msg.reply_to_message.photo)

async def gemini_text(_,__,msg: Message):
    """Check if the message starts with '/ask' and incase it's a reply to another message, that message should not contain a photo."""
    return msg.text and msg.text[:4] == '/ask' and not (msg.reply_to_message and msg.reply_to_message.photo)

sudo_users_filter = filters.create(sudo_check)
auth_chat_filter = filters.create(auth_check)
ask_text_filter = filters.create(gemini_text)
ask_img_filter = filters.create(gemini_img)