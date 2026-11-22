import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIDEO_ID = "1026421290532071"

flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "Bot is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask, daemon=True).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is Online! Use /send")

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_video(chat_id=update.effective_chat.id, video=VIDEO_ID)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
