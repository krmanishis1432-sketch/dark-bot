import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VIDEO_FILE_ID = "BAACAgUAAxkBAAI..." # aapka file_id yaha rahega, isko mat cherna agar pehle se hai

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Live hai! Video bhej raha hu...")
    # yaha video bhejne ka code
    # await update.message.reply_video(video=VIDEO_FILE_ID)

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

async def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

def main():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    asyncio.run(run_bot())

if __name__ == "__main__":
    main()
