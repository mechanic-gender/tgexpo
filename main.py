from html.parser import starttagopen

from jinja2.runtime import markup_join
from markupsafe import Markup
from telebot import types

from telebot.apihelper import forward_message

from const import TOKEN,TO_CHAT_ID
import telebot
bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def starter(msg):
    msg=bot.send_message(msg.chat.id,"privtcm ")
    bot.register_next_step_handler(msg,forward)
@bot.message_handler(commands=["stopt"])
def sto(msg):
    bot.send_message(msg.chat.id, "privtcmst")
    # bot.send_message(TO_CHAT_ID,"test")
    # bot.forward_message(TO_CHAT_ID, msg.chat.id, msg.message_id)
@bot.message_handler(content_types=["text"])
def text(msg1):
    if "anon" in msg1.text:
        bot.send_message(msg1.chat.id,"youre message was send")
        bot.send_message(TO_CHAT_ID, msg1.text)
    elif "knop" in msg1.text:
        markup=types.ReplyKeyboardMarkup()
        button1=types.KeyboardButton(text="call dima developer")
        markup.add(button1)
        bot.send_message(msg1.chat.id,"choose operation ",reply_markup=markup)
        bot.delete_message(msg1.chat.id,msg1.message_id)
    elif msg1.text=="call dima developer":
        bot.send_message(TO_CHAT_ID,"ave zmitrok vas prizivaut")
        bot.delete_message(msg1.chat.id,msg1.message_id)
    elif msg1.text == "call me aine kosher potts":
        bot.send_message(TO_CHAT_ID, "euda was activated")
        bot.send_message(msg1.chat.id, "dont credit me pls")

    else :
        bot.forward_message(TO_CHAT_ID, msg1.chat.id, msg1.message_id)
@bot.message_handler(content_types=["voice"])
def voice(msg2):
    bot.send_message(msg2.chat.id,"ew cant work width it")
    bot.reply_to(msg2,"votr tak")
@bot.message_handler(content_types=["video_note"])
def vdo(msg3):
    bot.send_message(msg3.chat.id,"yuo have nice home")


# def forward(message):
#     message=bot.forward_message(TO_CHAT_ID,message.chat.id,message.message_id)
#     bot.register_next_step_handler(message,second)
# def second(msg):
#     msg=bot.send_message(msg.chat.id,"sended")
#     bot.register_next_step_handler(msg,forward)
bot.infinity_polling()
