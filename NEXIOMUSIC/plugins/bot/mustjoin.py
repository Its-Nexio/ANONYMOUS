from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from NEXIOMUSIC import app

#--------------------------

SUPPORT_CHAT_ID = "ALL_SANATANI_BOT"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not SUPPORT_CHAT_ID:
        return
    try:
        try:
            await app.get_chat_member(SUPPORT_CHAT_ID, msg.from_user.id)
        except UserNotParticipant:
            link = f"https://t.me/{SUPPORT_CHAT_ID}"
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/cd02e62dea09e7514c45f.jpg", 
                    caption=f"๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ <a href={link}>๏ sᴜᴘᴘᴏʀᴛ ๏</a> ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ <a href={link}>๏ sᴜᴘᴘᴏʀᴛ ๏</a> ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏ Jᴏɪɴ ๏",  url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {SUPPORT_CHAT_ID}!")
