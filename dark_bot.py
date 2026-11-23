import os, threading, asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

# ===== YAHAN APNE LINK DALO =====
VIDEO_URL = "https://t.me/BANANA_X_HACK/2"  # Apni video ka link ya file_id daalo. Test ke liye direct mp4 link best hai
# Agar video file_id hai to aise: "BAACAgUAAxkBA..."
GET_KEY_URL = "https://t.me/+YOUR_KEY_LINK" # GET KEY ka blue link

CHANNELS = {
    "JOIN [1]": "https://t.me/channel1",
    "JOIN [2]": "https://t.me/channel2",
    "JOIN [3]": "https://t.me/channel3",
    "JOIN [4]": "https://t.me/channel4",
    "JOIN [5]": "https://t.me/channel5",
    "JOIN [6]": "https://t.me/channel6",
    "JOIN [7]": "https://t.me/channel7",
    "JOIN [8]": "https://t.me/channel8",
}
VOICE_URL = None # Agar voice bhejna hai to voice ka file_id daalo
# =================================

@app.route('/')
def home():
    return "Bot Live with Welcome Video!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1. Buttons banao
    buttons = []
    row = []
    i = 0
    for name, link in CHANNELS.items():
        row.append(InlineKeyboardButton(f"🔗 {name}", url=link))
        i+=1
        if i % 2 == 0:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    
    buttons.append([InlineKeyboardButton("✅ CHECK JOINED", callback_data="check_joined")])
    
    markup = InlineKeyboardMarkup(buttons)
    
    # 2. Message text - GET KEY blue link ke saath
    caption = f"""🔥 Welcome God 🥇

🚫 Join All Channels To Unlock 🔵

🔑 <a href="{GET_KEY_URL}">GET KEY</a>"""

    # 3. Video + Caption + Buttons bhejo
    try:
        # Video file_id ya URL se
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=VIDEO_URL,
            caption=caption,
            parse_mode="HTML",
            reply_markup=markup
        )
        # 4. Voice bhejo (agar hai to)
        # await context.bot.send_voice(chat_id=update.effective_chat.id, voice=VOICE_URL)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🔊 Voice: Join all channels then press CHECK!",
        )
    except Exception as e:
        # Agar video fail ho to sirf text bhejo
        await update.message.reply_text(caption, parse_mode="HTML", reply_markup=markup)
        print(f"Video Error: {e}")

async def check_joined_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # Yahan check logic laga sakte ho - user ne join kiya ya nahi
    # Abhi ke liye simple reply
    await query.message.reply_text("✅ Checking... All channels joined? Here is your key: 🔑\n" + GET_KEY_URL)

def run_bot():
    if not BOT_TOKEN:
        print("BOT_TOKEN missing!")
        return
    async def main():
        from telegram import Bot
        bot = Bot(token=BOT_TOKEN)
        await bot.delete_webhook(drop_pending_updates=True)
        
        app_bot = Application.builder().token(BOT_TOKEN).build()
        app_bot.add_handler(CommandHandler("start", start))
        app_bot.add_handler(CallbackQueryHandler(check_joined_callback, pattern="check_joined"))
        
        await app_bot.initialize()
        await app_bot.start()
        await app_bot.updater.start_polling()
        print("Bot with Video Welcome Started!")
        while True:
            await asyncio.sleep(3600)
    asyncio.run(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
