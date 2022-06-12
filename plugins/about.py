
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("Bot :- @ASMODS_Rename_Bot\nCreater :- @ERROR_X_PREDATOR\Language :-Python3\nLibrary :- Pyrogram 1.4.16\nServer :- Heroku")
