import os
import openai
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.utils import executor

# initialize the OpenAI API client
openai.api_key = os.environ.get('OPENAI_KEY')
tg_api_key = os.environ.get('TG_KEY')

# initialize the Telegram bot
bot = aiogram.Bot(token=tg_api_key)
dp = Dispatcher(bot)

# context variable to store information about the current conversation
context = {}

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.reply("Hello! How can I help you today?")

@dp.message_handler()
async def echo_message(message: Message):
    # use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{context.get('prompt', '')} {message.text}",
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )
    # update the context with the current message
    context['prompt'] = f"{context.get('prompt', '')} {message.text}"
    # send the response
    await message.reply(response.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
