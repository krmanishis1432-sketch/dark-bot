import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Live - Video Ready!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ruko, video bhej raha hu 🔥")
    try:
        with open("video.mp4", "rb") as video_file:
            await update.message.reply_video(video=video_file, caption="🔥 Free Fire Gameplay - Dark Bot")
    except FileNotFoundError:
        await update.message.reply_text("Error: video.mp4 file GitHub pe upload nahi hai! Add file > Upload files se upload karo.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", start))
    print("Bot Started...")
    application.run_polling()

if __name__ == "__main__":
    main()
