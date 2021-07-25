import telebot
# Import

bot = telebot.TeleBot('your token from @BotFather')
# Token

@bot.message_handler(commands=['start'])
def start_cmd(message):
	bot.send_message(message.chat.id, 'Привет, %s!' % message.from_user.username)
# Command start

@bot.message_handler(commands=['say'])
def say_cmd(message):
	if message.chat.id != 1538017618:
		name = message.from_user.username
		args = message.text.replace('/say ', '')
		args = str(args) + ' [ ' + str(name) + ', ' + str(message.chat.id) + ' ]'
		bot.send_message(message.chat.id, args)
	else:
		bot.send_message(message.chat.id, 'У вас заблокирована эта команда, попросите администратора о разблакировке.')
# Command say

bot.polling(none_stop=True)
