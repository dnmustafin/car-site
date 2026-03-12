import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8775611491:AAE1H4MzGFh7iSLzj5zmARktBPRI4iI9n0k"
SITE_URL = "https://dnmustafin.github.io/car-showroom/"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🚗 *Наш автосалон*\n\n"
        f"Сайт: {SITE_URL}\n\n"
        f"Нажмите на ссылку чтобы открыть",
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен со ссылкой на сайт")
    app.run_polling()

if __name__ == "__main__":
    main()