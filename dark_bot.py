import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)
VIDEO_ID_FILE = "video_id.txt"

@app.route('/')
def home():
    return "Bot Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is Online! ✅")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

async def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN not found!")
        return
    
    # Flask ko alag thread me chalao
    threading.Thread(target=run_flask, daemon=True).start()
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot Started...")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
