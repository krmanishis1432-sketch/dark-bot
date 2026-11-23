import os, threading, asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

GET_KEY_URL = "https://t.me/+wS7sgzAEfLo4N2Vl"

# VIDEO - Isko baad me bharenge Gallery se upload karke
VIDEO_ID = ""

CH1 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH2 = "https://t.me/BananaKingOfficial1"
CH3 = "https://t.me/+-OVs01otc_owZmE9"
CH4 = "https://t.me/BananaKingOfficial1"
CH5 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH6 = "https://t.me/+wS7sgzAEfLo4N2Vl"
CH7 = "https://t.me/+wS7sgzAEfLo4N2Vl"

@app.route('/')
def home():
    return "Bot Live - Video Ready"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("JOIN [1]", url=CH1), InlineKeyboardButton("JOIN [2]", url=CH2)],
        [InlineKeyboardButton("JOIN [3]", url=CH3), InlineKeyboardButton("JOIN [4]", url=CH4)],
        [InlineKeyboardButton("JOIN [5]", url=CH5), InlineKeyboardButton("JOIN [6]", url=CH6)],
        [InlineKeyboardButton("JOIN [7]", url=CH7)],
        [InlineKeyboardButton("CHECK JOINED", callback_data="check")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    text = f"Welcome God\n\nJoin All Channels To Unlock\n\nGET KEY: {GET_KEY_URL}"
    
    try:
        if VIDEO_ID:
            await context.bot.send_video(chat_id=update.effective_chat.id, video=VIDEO_ID, caption=text, reply_markup=markup)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=markup, disable_web_page_preview=True)
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=markup, disable_web_page_preview=True)

async def check_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text(f"Key Unlocked: {GET_KEY_URL}")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        fid = update.message.video.file_id
        await update.message.reply_text(f"VIDEO ID MIL GAYA ✅\n\nCopy karo:\n\n`{fid}`\n\nIsko GitHub me VIDEO_ID me daal do!", parse_mode="Markdown")
        # Preview bhi bhej do
        await context.bot.send_video(chat_id=update.effective_chat.id, video=fid, caption="Ye video ab /start pe ayega!")
    if update.message.animation:
        fid = update.message.animation.file_id
        await update.message.reply_text(f"ANIMATION ID:\n`{fid}`", parse_mode="Markdown")
    if update.message.voice:
        fid = update.message.voice.file_id
        await update.message.reply_text(f"VOICE ID:\n`{fid}`", parse_mode="Markdown")

def run_bot():
    if not BOT_TOKEN:
        return
    async def main():
        from telegram import Bot
        await Bot(token=BOT_TOKEN).delete_webhook(drop_pending_updates=True)
        app_bot = Application.builder().token(BOT_TOKEN).build()
        app_bot.add_handler(CommandHandler("start", start))
        app_bot.add_handler(CallbackQueryHandler(check_button, pattern="check"))
        app_bot.add_handler(MessageHandler(filters.VIDEO | filters.ANIMATION | filters.VOICE, get_id))
        await app_bot.initialize()
        await app_bot.start()
        await app_bot.updater.start_polling()
        while True:
            await asyncio.sleep(3600)
    asyncio.run(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
