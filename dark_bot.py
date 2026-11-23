import os
import threading
import asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

GET_KEY_URL = "https://t.me/+wS7sgzAEfLo4N2Vl"

CH1 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH2 = "https://t.me/BananaKingOfficial1"
CH3 = "https://t.me/+-OVs01otc_owZmE9"
CH4 = "https://t.me/BananaKingOfficial1"
CH5 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH6 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH7 = "https://t.me/+wS7sgzAEfLo4N2Vl"

@app.route('/')
def home():
    return "Bot is Live"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("JOIN [1]", url=CH1), InlineKeyboardButton("JOIN [2]", url=CH2)],
        [InlineKeyboardButton("JOIN [3]", url=CH3), InlineKeyboardButton("JOIN [4]", url=CH4)],
        [InlineKeyboardButton("JOIN [5]", url=CH5), InlineKeyboardButton("JOIN [6]", url=CH6)],
        [InlineKeyboardButton("JOIN [7]", url=CH7)],
        [InlineKeyboardButton("CHECK JOINED", callback_data="check")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    text = "Welcome God\n\nJoin All Channels To Unlock\n\nGET KEY: " + GET_KEY_URL
    html_text = f'<b>Welcome God</b>\n\nJoin All Channels To Unlock\n\n<a href="{GET_KEY_URL}">GET KEY</a>'
    await update.message.reply_text(html_text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True)

async def check_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Key: " + GET_KEY_URL)

def run_bot():
    if not BOT_TOKEN:
        print("BOT_TOKEN missing")
        return
    async def main():
        from telegram import Bot
        b = Bot(token=BOT_TOKEN)
        await b.delete_webhook(drop_pending_updates=True)
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(check_button, pattern="check"))
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        print("Bot Started")
        while True:
            await asyncio.sleep(3600)
    asyncio.run(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
