from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import api_id,api_hash,bot_token,mongo_uri

plugins = dict(root='bot/plugins')

bot = Client(name='gemini-bot',
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token, plugins=plugins)

clientdb = AsyncIOMotorClient(mongo_uri)