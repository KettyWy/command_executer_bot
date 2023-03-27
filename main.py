import os
import subprocess
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
LIST_ID = os.getenv('LIST_ID').split(',')
bot = telebot.TeleBot(TOKEN)
COMMAND_LIST = {
    'dir': 'dir',
    'date': 'date /T',
    'whoami': 'WHOAMI',
}


@bot.message_handler(commands=COMMAND_LIST.keys())
def start_message(message):
    if str(message.from_user.id) in LIST_ID:
        res = commands(message.text.replace("/", ""))
        bot.reply_to(message, str(res))
    else:
        bot.reply_to(message, 'В доступе отказано!')


def commands(commands):
    if commands in COMMAND_LIST.keys():
        result = subprocess.run(COMMAND_LIST[commands], shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='cp866'
                                )
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    else:
        return 'Неизвестная команда.'
if __name__ == '__main__':
    bot.infinity_polling()
    # print(commands(['ls']))
    # print(commands(['dir']))
    # print(test(['dir', '/A:-D']))
    # print(commands(['dir', '/T:W']))
