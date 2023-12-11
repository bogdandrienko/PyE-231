import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
Привет, я бот, поговори со мной!

Команды:
/approve
""")


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.chat.username, update.message.chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
<strong>Вы подписаны на обновления!</strong>
""", parse_mode="html")


if __name__ == '__main__':
    """
    @BotFather
    /newbot
    save token and link
    pip install python-telegram-bot
    """
    application = ApplicationBuilder().token("6669581355:AAEcK9yBwL_D2tZi8W6zUVup04STZYkStIE").build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('approve', approve))
    #
    print("bot started")
    application.run_polling()  # блокирующая(код ниже в этом потоке исполнения не идёт)
    print("bot stopped")
