import asyncio
from telethon import TelegramClient

api_id = 32264055  # put your api id
api_hash = "4445cb8837433b7fc7033f7f2219eae7"

client = TelegramClient("user_session", api_id, api_hash)

async def send_otp(phone):
    await client.connect()
    await client.send_code_request(phone)

async def verify_otp(phone, code):
    await client.sign_in(phone, code)
    me = await client.get_me()
    return me.id
