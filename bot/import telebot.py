import telebot
from mess import hello
from mess import purch

# Создаем экземпляр бота
bot = telebot.TeleBot('5493646832:AAEd2_h_fOBkKoSgi83xaAxS2jYjAzApwRo')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start', 'help'])
def start(m, res=False):
    if m.text == '/start':
        bot.send_message(m.chat.id, 'Введите текст')
    else:
        bot.send_message(m.chat.id, 'Тут должна быть помощь')
        
    
#Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text in ['привет', 'Привет']:
        bot.send_message(message.chat.id, f'{hello()} {str(message.chat.username)}')
        
        
    else:    
        bot.send_message(message.chat.id, 'Ну я даже не знаю что вам ответить!')# + message.text)


#получение документа(json)
@bot.message_handler(content_types=['document'])
def handle_docs_doc(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = r'C:\Users\Алексей Савелов\Downloads\Telegram Desktop\check\\' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        purch(name=src)
        
        bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)        
        

        
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.reply_to(message, "Я только учусь")

    
    
# Запускаем бота
bot.polling(none_stop=True, interval=0)