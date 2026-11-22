import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)
VIDEO_ID_FILE = "video_id.txt"

@app.route('/')
def home():
    return "Bot Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(VIDEO_ID_FILE):
        with open(VIDEO_ID_FILE, "r") as f:
            file_id = f.read().strip()
        await update.message.reply_video(video=file_id, caption="🔥 Free Fire - Dark Bot")
    else:
        await update.message.reply_text("Pehle mujhe Free Fire wala video bhejo, fir /start pe bhejunga!")

async def save_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.video.file_id
    with open(VIDEO_ID_FILE, "w") as f:
        f.write(file_id)
    await update.message.reply_text("Save ho gaya! ✅ Ab /start likho.")

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.VIDEO, save_video))
    application.add_handler(CommandHandler("start", start))
    print("Bot Started...")
    application.run_polling()

if __name__ == "__main__":
    main()
