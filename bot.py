import config
import asyncio

from telebot.async_telebot import AsyncTeleBot
from random import choice
bot = AsyncTeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['info'])
async def info_bot(message):
    text = "вот список комманд бота: help:'помошь', start:'запуск программы', fact:'случайный интерестный факт'"
    await bot.reply_to(message, text)


@bot.message_handler(commands=['fact'])
async def random_fact(message):
    text = choice(["В языке древних греков не существовало слова, которое обозначало религию.", "Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.", 
                   "Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.", 
                   "У медуз нет мозгов и кровеносных сосудов.", "Кошки спят больше половины своей жизни."])
    await bot.reply_to(message, text)
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())