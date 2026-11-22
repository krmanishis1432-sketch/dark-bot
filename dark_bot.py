import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# Neeche apna File_ID aane ke baad dalenge
VIDEO_FILE_ID = None  

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if VIDEO_FILE_ID:
        await update.message.reply_video(video=VIDEO_FILE_ID, caption="Lo bhai 🔥")
    else:
        await update.message.reply_text("Bot Live hai! Ab mujhe Telegram pe ye video bhejo, mai File_ID de dunga.")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.video.file_id
    print(f"FILE ID MILA: {file_id}")
    await update.message.reply_text(f"Ye raha File ID, isko copy karo:\n\n`{file_id}`\n\nIsko GitHub me VIDEO_FILE_ID me paste kar do.", parse_mode='Markdown')
    # turant video wapas bhi bhej dega test ke liye
    await update.message.reply_video(video=file_id)

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.VIDEO, get_file_id))
    application.run_polling()

if __name__ == "__main__":
    main()
