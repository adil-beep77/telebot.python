import telebot

TOKEN = '8288245617:AAF6W0Qvy-ometWxCnAXHJGFU52YEgle9Y4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('gucci')
    button2 = telebot.types.KeyboardButton('perfume')
    button3 = telebot.types.KeyboardButton('Video-Nike')
    button4 = telebot.types.KeyboardButton('Help')
    button5 = telebot.types.KeyboardButton('Audio')
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)

# Обработчик нажатия на кнопку "gucci"
@bot.message_handler(func=lambda message: message.text == 'gucci')
def send_nike(message):
    # Отправка изображения
    with open('Без названия (1).jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")

@bot.message_handler(func=lambda message: message.text == 'perfume')
def send_nike(message):
    # Отправка изображения
    with open('Duhi.png', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="бул жакшы духи окшойт!")

# Обработчик нажатия на кнопку "Video-Nike"
@bot.message_handler(func=lambda message: message.text == 'Video-Nike')
def send_video_nike(message):
    # Отправка видео
    with open('Без названия.png', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео.")

# Обработчик нажатия на кнопку "Help"
@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    # Отправка сообщения со справкой
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")


# Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Audio')
def send_audio(message):
    # Отправка аудиосообщения
    with open('', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

# Запуск бота
bot.polling()

