#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝙠𝙮𝙖 𝙗𝙝𝙖𝙞 𝙠𝙮𝙖 𝙝𝙪𝙖 𝙠𝙮𝙪 𝙗𝙤𝙩 𝙠𝙚 𝙜𝙖𝙣𝙙 𝙢𝙖𝙧 𝙧𝙖𝙝 𝙝𝙖𝙞<b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("😊 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
