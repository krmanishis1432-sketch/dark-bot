import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# Apna asli video file_id yaha paste karo - pura hona chahiye
VIDEO_FILE_ID = "BAACAgUAAxkBAAI4... pura ID yaha" 

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_video(video=VIDEO_FILE_ID, caption="Lo bhai video 😈")
    except Exception as e:
        await update.message.reply_text(f"Video bhejne me error: {e}\nFile ID check karo")

def main():
    # Flask ko alag thread me chalana
    import threading
    def run_flask():
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    
    threading.Thread(target=run_flask, daemon=True).start()

    # Bot start
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
