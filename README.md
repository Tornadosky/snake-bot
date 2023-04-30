# Snake-Bot

The idea of the project is a Telegram bot, that can classify 3 most common snakes in Eastern Europe.

At the moment, the classifier recognizes 3 types of snakes:
- **Grass snake** (natrix) (Common, water);
- **Viper** (Common, Steppe, Nikolski's, Dinnick's);
- **Copperheads**.

It can also determine the absence of a snake in the image. The selected 3 types of snakes are the most common in Eastern Europe.

Telegram bot is accessible [here](https://t.me/aka_snake_bot). To test it out you need to send an image (not file, but an image). The bot will respond with the predicted result.
<p float="left">
  <img src="https://user-images.githubusercontent.com/109428348/235349599-143ed911-35b0-47ae-bf3f-268ea4144987.jpg" width="300">
  <img src="https://user-images.githubusercontent.com/109428348/235349604-686709a1-aa6e-419f-8891-960294548bc6.jpg" width="300">
</p>
Examples of model predictions (images from test set, text - model predictions):

![image](https://user-images.githubusercontent.com/109428348/235349735-cd2af4a2-e11b-491c-8d46-7ecc6e7aeda4.png)
