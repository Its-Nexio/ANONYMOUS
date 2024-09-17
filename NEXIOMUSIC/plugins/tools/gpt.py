import asyncio
import aiohttp
from pyrogram import Client, filters
from NEXIOMUSIC import app
from pymongo import MongoClient
from config import MONGO_DB_URI

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

async def chat_with_api(question):
    url = f"https://chatgpt.apiitzasuraa.workers.dev/?question={question}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data["code"] == 2:
                    return data["content"]
                else:
                    return "ᴇʀʀᴏʀ: ᴜɴᴀʙʟᴇ ᴛᴏ ɢᴇᴛ ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ ᴛʜᴇ ᴀᴘɪ"
            else:
                return "ᴇʀʀᴏʀ: ᴜɴᴀʙʟᴇ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴛʜᴇ ᴀᴘɪ"
                
@app.on_message(filters.command(["chatgpt","ai","ask","gpt","solve"],  prefixes=["/", ".", "!", "?"]))
async def gptAi(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        await message.reply_text("❖ ᴜꜱᴀɢᴇ : /ai [ǫᴜᴇʀʏ]")
    else:
        response = await chat_with_api("gpt", split_text[1])
        await message.reply_text(response)
