import os
import telebot
import json
import io
import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from PIL import Image

# Key is stored in config.json file
config = json.load(open("config.json"))
BOT_TOKEN = config["BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)

WELCOME_MSG = """Hello, I am Snaky. I can classify 3 species of snake if you provide me the image.
 I know vipers, grass snakes and copperheads."""
ECHO_MSG = """I can only classify snakes in images.
 Attach an image and I'll try to understand what kind of snake it is."""

classes = {0: 'Natrix', 1: 'Vipera', 2: 'Coronella', 3: 'No snakes'}
model_path = os.path.abspath(os.getcwd() + "/model")
print(model_path)

# Define a model
model = keras.models.load_model(model_path, custom_objects=None, compile=True, options=None)


def predict_snake(img):
    # Prepare an image
    img = Image.open(io.BytesIO(img))
    img = img.convert('RGB')
    img = img.resize((224, 224), Image.NEAREST)
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    final_image = keras.applications.densenet.preprocess_input(img_array_expanded_dims)

    # Make a prediction
    pred = np.argmax(model.predict(final_image))

    # Map number to text with shakes breed
    predicted_snake = classes[pred]
    return predicted_snake


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, WELCOME_MSG)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, ECHO_MSG)


bot.infinity_polling()
