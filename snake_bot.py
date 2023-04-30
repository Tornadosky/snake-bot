import os
import telebot
import json

# Key is stored in config.json file
config = json.load(open("config.json"))
BOT_TOKEN = config["BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)

WELCOME_MSG = """Hello, I am Snaky. I can classify 3 species of snake if you provide me the image.
 I know vipers, grass snakes and copperheads."""
ECHO_MSG = """I can only classify snakes in images. Attach an image and I'll try to understand what kind of snake it is."""


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, WELCOME_MSG)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, ECHO_MSG)


bot.infinity_polling()
