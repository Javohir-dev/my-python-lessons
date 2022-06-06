from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = "5217388063:AAHHEWAvkhb8tUtLox74PHb1BaMY-rTO0lQ"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu aleykum, hush kelibsiz!"
    javob += "\nMatn kiriting."
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    def javob(msg): return to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.infinity_polling()

# matn = input("Matin kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
