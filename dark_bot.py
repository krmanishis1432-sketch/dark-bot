import os
import threading
import traceback
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
print(f"BOT_TOKEN found: {bool(BOT_TOKEN)}")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Live! Working Fine! Token Set: " + str(bool(BOT_TOKEN))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot Online Hai! Final Fix Working!")

def run_bot():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN is missing! Set it in Render Environment Variables!")
        return
    try:
        print("Starting Telegram Bot...")
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        print("Bot Started... Polling...")
        application.run_polling()
    except Exception as e:
        print(f"Bot Error: {e}")
        traceback.print_exc()

# Bot ko background me chalao, Flask ko main me
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting Flask on port {port}")
    app.run(host='0.0.0.0', port=port)
