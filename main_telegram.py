from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, filters, MessageHandler, ContextTypes, CallbackQueryHandler
from first import get_playbill
from dotenv import load_dotenv
import os 
import re 
from datetime import datetime, timedelta

load_dotenv() # загрузка переменных из окружения .env
token_my = os.getenv("token_bot")


async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет. Я бот, который может показать сеансы фильмов на определенную дату. Необходимо ввести дату в формате гггг-мм-дд. Например: 2026-08-02')


async def reply_with_info(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()
    date_pattern = r'^\d{4}-\d{2}-\d{2}' # шаблон для проверки формата даты
    if not re.match(date_pattern, user_message):
        await update.message.reply_text('Неверный формат даты. Нужно в формате гггг-мм-дд. Пример: 2026-08-01')
        return 
    playbill = get_playbill(user_message)
    if not playbill:
        await update.message.reply_text('Сеансов нет на эту дату')
    else:
        await update.message.reply_text('\n'.join(playbill))


async def tomorrow(update:Update, context:ContextTypes.DEFAULT_TYPE):
    tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    playbill = get_playbill(tomorrow_date)
    if not playbill:
        await update.message.reply_text('Сеансов на завтра нет')
    else:
        await update.message.reply_text('\n'.join(playbill))

async def button(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    


def main():
    application = Application.builder().token(token_my).build() # создание объекта приложения бота
    application.add_handler(CommandHandler('start', start)) # обработчик для команды старт
    application.add_handler(CommandHandler('tomorrow', tomorrow)) # обработчик для команды завтра
    application.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND, reply_with_info)) # обработчик сообщений
    print('Бот запущен')
    application.run_polling() # запуск самого бота


if __name__ == "__main__":
    main()