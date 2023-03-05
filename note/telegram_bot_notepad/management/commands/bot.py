import telebot
from telebot import types
from django.core.management.base import BaseCommand
# импорт работает, используется Notepad бд
from notepad.models import Notepad

TOKEN = "6207508766:AAGGM21zo8YFhxlGUOU0_6tRAu6Cazps2SQ"
bot = telebot.TeleBot(TOKEN)


# создаём комманду для запуска через manage.py
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()
        bot.infinity_polling()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 '''Привет.
Теперь я твой новый блокнот.
Вноси новую информацию и она останется тут. ''')
    chat_id = message.chat.id
    menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = types.KeyboardButton('Показать список записей')
    button_new_note = types.KeyboardButton('Создать новую запись')
    menu_buttons.add(button_list, button_new_note)
    bot.send_message(chat_id, 'Выбирай: ', reply_markup=menu_buttons)


@bot.message_handler(content_types=['text'])
def list_note(message):

    if message.text == 'Назад':
        send_welcome(message)

    if message.text == 'Показать список записей':
        notes = Notepad.objects.all()
        menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for note in notes:
            button_note = types.KeyboardButton(str(note.id) + '. ' + note.heading)
            menu_buttons.add(button_note)
        button_return = types.KeyboardButton('Назад')
        menu_buttons.add(button_return)
        bot.send_message(message.chat.id, 'Список: ', reply_markup=menu_buttons)


