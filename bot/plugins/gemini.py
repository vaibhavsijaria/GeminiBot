from pyrogram import Client, filters
from pyrogram.types import Message
from bot.helper.filters import auth_chat_filter, ask_img_filter, ask_text_filter
from bot.config import gemini_api
from PIL import Image
import google.generativeai as genai
import asyncio

genai.configure(api_key=gemini_api)

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

@Client.on_message(ask_text_filter)
async def gemini_text(client: Client, message: Message):
    model = genai.GenerativeModel('gemini-pro')
    response = await model.generate_content_async(
        message.text,
        stream=True,
        safety_settings=safety_settings
    )
    message = await message.reply('Generating response ..')
    answer = ''
    async for chunk in response:
        await message.edit_text(answer := (answer + chunk.text))

@Client.on_message(ask_img_filter)
async def gemini_img(client: Client, message: Message):
    msg = await message.reply('Generating response ..')
    model = genai.GenerativeModel('gemini-pro-vision')
    if message.reply_to_message:
        photo = await message.reply_to_message.download(in_memory=True)
        text = message.text[4:]
    else:
        photo = await message.download(in_memory=True)
        text = message.caption[4:]
    photo = Image.open(photo)
    await msg.edit_text('Loaded image ..')
    response = await model.generate_content_async(
        [text, photo],
        stream=True,
        safety_settings=safety_settings
    )
    answer = ''
    async for chunk in response:
        await msg.edit_text(answer := (answer + chunk.text))