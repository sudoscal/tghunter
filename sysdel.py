from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для удаления системных сообщений
async def delete_system_messages(update: Update, context: CallbackContext):
    # Проверяем, является ли сообщение системным (о вступлении или выходе пользователя)
    if update.message.left_chat_member or update.message.new_chat_members:
        # Удаляем сообщение
        await update.message.delete()

# Функция для добавления рекламного сообщения
async def add_advertisement(update: Update, context: CallbackContext):
    # Проверяем, является ли сообщение командой /advertise
    if update.message.text == "/advertise":
        # Отправляем рекламное сообщение
        await context.bot.send_message(chat_id=update.message.chat_id, text="Ваше рекламное сообщение здесь!")

# Функция для обработки ошибок
async def error(update: Update, context: CallbackContext):
    logger.warning(f'Update {update} caused error {context.error}')

# Основная функция
def main():
    # Вставьте сюда ваш токен
    token = '******************'

    # Создаем Application и передаем ему токен вашего бота
    application = Application.builder().token(token).build()

    # Регистрируем обработчик для удаления системных сообщений
    application.add_handler(MessageHandler(filters.StatusUpdate.ALL, delete_system_messages))

    # Регистрируем обработчик для добавления рекламных сообщений
    application.add_handler(CommandHandler("advertise", add_advertisement))

    # Регистрируем обработчик ошибок
    application.add_error_handler(error)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
