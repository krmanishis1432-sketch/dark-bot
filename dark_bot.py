import os, threading, asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

GET_KEY_URL = "https://t.me/+wS7sgzAEfLo4N2Vl" # AAPKA GET KEY LINK

CHANNELS = [
    ("JOIN [1]", "https://t.me/+wS7sgzAEfLo4N2Vl"),
    ("JOIN [2]", "https://t.me/BananaKingOfficial1"),
    ("JOIN [3]", "https://t.me/+-OVs01otc_owZmE9"),
    ("JOIN [4]", "https://t.me/BananaKingOfficial1"),
    ("JOIN [5]", "https://t.me/+wS7sgzAEfLo4N2Vl"),
    ("JOIN [6]", "https://t.me/+wS7sgzAEfLo4N2Vl"),
    ("JOIN [7]", "https://t.me/+wS7sgzAEfLo4N2Vl"),
]

@app.route('/')
def home():
    return "Banana X Hack Live"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton(f"🔗 {CHANNELS[0][0]}", url=CHANNELS[0][1]), InlineKeyboardButton(f"🔗 {CHANNELS[1][0]}", url=CHANNELS[1][1])],
        [InlineKeyboardButton(f"🔗 {CHANNELS[2][0]}", url=CHANNELS[2][1]), InlineKeyboardButton(f"🔗 {CHANNELS[3][0]}", url=CHANNELS[3][1])],
        [InlineKeyboardButton(f"🔗 {CHANNELS[4][0]}", url=CHANNELS[4][1]), InlineKeyboardButton(f"🔗 {CHANNELS[5][0]}", url=CHANNELS[5][1])],
        [InlineKeyboardButton(f"🔗 {CHANNELS[6][0]}", url=CHANNELS[6][1])],
        [InlineKeyboardButton("✅ CHECK JOINED", callback_data="check")]
    ]
    markup = InlineKeyboardMarkup(buttons)
    text = f'🔥 Welcome God 🥇\n\n🚫 Join All Channels To Unlock 🔵\n\n🔑 <a href="{GET_KEY_URL}">GET KEY</a>'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True)

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text(f"✅ Key Unlocked 🗝️\n{GET_KEY_URL}")

def run_bot():
    if not BOT_TOKEN: return
    async def main():
        from telegram import Bot
        await (Bot(token=BOT_TOKEN)).delete_webhook(drop_pending_updates=True)
        app_bot = Application.builder().token(BOT_TOKEN).build()
        app_bot.add_handler(CommandHandler("start", start))
        app_bot.add_handler(CallbackQueryHandler(check, pattern="check"))
        await app_bot.initialize()
        await app_bot.start()
        await app_bot.updater.start_polling()
        while True: await asyncio.sleep(3600)
    asyncio.run(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)
