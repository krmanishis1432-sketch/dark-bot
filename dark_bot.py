import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return f"BOT Token Set: {bool(BOT_TOKEN)} - BOT IS LIVE"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ON hai. /send likho.")

# /send command
async def send_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send command working!")

def run_bot():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing in Render Environment!")
        return
    
    print("Starting Bot...")
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_cmd))

    # Run polling
    application.run_polling()

if __name__ == "__main__":
    # Bot ko alag thread me chalao
    threading.Thread(target=run_bot, daemon=True).start()
    # Flask ko chalao taaki Render live samjhe
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
