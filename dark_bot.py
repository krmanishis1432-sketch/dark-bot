import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

@app.route('/')
def home():
    return f"BOT Token Set: {bool(BOT_TOKEN)} | Bot is Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ON hai. /send likho.")

async def send_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bhejo kya send karna hai? Video / Photo bhejo, mai forward kar dunga!")

def run_bot():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing!")
        return
    print("Bot Starting...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_cmd))
    print("Bot Started Polling...")
    application.run_polling()

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
