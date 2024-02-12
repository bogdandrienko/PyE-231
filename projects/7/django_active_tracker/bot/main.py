from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {update.effective_user.id}')


def main():
    print("\n...bot started...")

    app = ApplicationBuilder().token("6589285143:AAF_jOEz0-eFpX3MeBSc49aK9Zw3W7NQbtc").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
