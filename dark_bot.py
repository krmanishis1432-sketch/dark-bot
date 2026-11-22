from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8305021240:AAH..._TUMHARA_TOKEN_YAHAN_DALO"
VIDEO_ID = "1026421290532071"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ON hai. /send likho.")

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_video(chat_id=update.effective_chat.id, video=VIDEO_ID, caption="Phone off par bhi chalega!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send))
    app.run_polling()

if __name__ == "__main__":
    main()
