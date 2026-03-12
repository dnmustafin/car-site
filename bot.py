import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8775611491:AAE1H4MzGFh7iSLzj5zmARktBPRI4iI9n0k"
SITE_URL = "https://dnmustafin.github.io/car-showroom/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🚗 *Наш автосалон*\n\n"
        f"Сайт: [Нажмите чтобы открыть]({SITE_URL})\n\n"
        f"📍 Москва, ул. Автомобильная, 1\n"
        f"📞 +7 (999) 123-45-67",
        parse_mode='Markdown'
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("✅ Бот готов!")
app.run_polling()