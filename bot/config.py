from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')

api_id = getenv('tele_api_id')
api_hash = getenv('tele_api_hash')
bot_token = getenv('bot_token')

mongo_uri = getenv('mongodb_uri')

sudo_usr = getenv('sudo_usr').split(' ')
sudo_usr = list(map(lambda x:int(x),sudo_usr))

auth_chats = getenv('auth_chats').split(' ')
auth_chats = list(map(lambda x:int(x),auth_chats)) + sudo_usr
log_channel = int(getenv('log_channel'))

download_path = getenv('download_path')

gemini_api = getenv('gemini_api')