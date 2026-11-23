import os
import threading
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

@app.route('/')
def home():
    return f"BOT Token Set: {bool(BOT_TOKEN)} - Bot is Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ON hai! /send use karo ✅")

async def send_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send command ready!")

def run_bot():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing in Render!")
        return
    print("Starting Bot...")
    # Webhook delete karke polling start karo
    async def delete_webhook_and_run():
        # Pehle webhook delete
        from telegram import Bot
        bot = Bot(token=BOT_TOKEN)
        await bot.delete_webhook(drop_pending_updates=True)
        print("Webhook deleted!")
        
        # Fir polling start
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("send", send_cmd))
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        print("Bot polling started!")
        # Keep running
        while True:
            await asyncio.sleep(3600)

    asyncio.run(delete_webhook_and_run())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
