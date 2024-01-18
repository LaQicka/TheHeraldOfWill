import telebot
import GPT

def readToken():
    with open('config.txt', 'r') as f:
        return f.read()

TOKEN = readToken()
bot = telebot.TeleBot(TOKEN)


# def getHistory(update: telebot.types.Update, context: telebot.CallbackContext) -> None:
#     chat_id = update.message.chat_id
#     # Получаем список сообщений в чате
#     message_list = context.bot.get_chat_history(chat_id, limit=5)
#     # Сохраняем текст каждого сообщения
#     messages_text = [message.text for message in message_list]
#     # Отправляем список последних 5 сообщений обратно пользователю
#     update.message.reply_text('\n'.join(messages_text))

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Внимай смерд, ибо пред тобой Вестник UnitedMordor! Если осмелишься спросить - отвечу на любой вопрос.")

# Обработчик для эхо-функции текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я вниму твоим мольбам. Наберись терпения")
    
    try:
        response = GPT.ask_gpt_4(message.text)
        bot.reply_to(message, response)
    
    except:
        answer = "Произошла ошибка. Попробуйте ещё раз"
        bot.reply_to(message, answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)    