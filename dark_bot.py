import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VIDEO_FILE_ID = os.environ.get("VIDEO_FILE_ID")  # ab env se lenge

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live! Fix is Done"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if VIDEO_FILE_ID:
        await update.message.reply_video(video=VIDEO_FILE_ID, caption="Lo bhai 🔥 Free Fire!")
    else:
        await update.message.reply_text("Bot fix ho gaya! Ab mujhe Telegram pe video bhejo, mai ID de dunga.")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.video.file_id
    await update.message.reply_text(f"ID mil gaya! Copy karo:\n\n{file_id}")

# Bot setup
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.VIDEO, get_file_id))

@app.route('/webhook')
async def webhook_runner():
    await application.initialize()
    await application.start()
    return "ok"

def main():
    # Flask alag thread me nahi, simple rakho
    import threading
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000))), daemon=True).start()
    application.run_polling()

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing!")
    else:
        main()
