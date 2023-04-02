import telebot
from telebot import types
from django.core.management.base import BaseCommand
# импорт работает, используется Notepad бд
from notepad.models import Notepad

TOKEN = "6207508766:AAGGM21zo8YFhxlGUOU0_6tRAu6Cazps2SQ"
bot = telebot.TeleBot(TOKEN)

back = 'Назад'
list = 'Список: '
all_list = 'Показать список записей'
new_note = 'Создать новую запись'
choose = 'Выбирай: '


# создаём команду для запуска через manage.py
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()


notes = Notepad.objects.all()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'''Привет, {message.from_user.username}.\nТеперь я твой новый блокнот. 
    \nВноси новую информацию и она останется тут. ''')
    chat_id = message.chat.id
    menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = types.KeyboardButton(all_list)
    button_new_note = types.KeyboardButton(new_note)
    menu_buttons.add(button_list, button_new_note)
    bot.send_message(chat_id, choose, reply_markup=menu_buttons)


@bot.message_handler(content_types=['text'])
def list_note(message):
    if message.text == back:
        send_welcome(message)

    for note in notes:
        if message.text == note.heading:
            bot.reply_to(message, note.text)

    if message.text == all_list:
        menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for note in notes:
            button_note = types.KeyboardButton(text=note.heading)
            menu_buttons.add(button_note)
        button_return = types.KeyboardButton(back)
        menu_buttons.add(button_return)
        bot.send_message(message.chat.id, list, reply_markup=menu_buttons)

    # if message.text == new_note:
        # note = Notepad()
        # note.heading = message.text
        # note.save()
        # print('1111')


bot.infinity_polling()
