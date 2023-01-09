import settings
from aiogram import types, executor, Dispatcher, Bot
import openai

openai.api_key = settings.CHATGPTTOKEN
bot = Bot(token=settings.BOTTOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nSend me a request to start")

@dp.message_handler()
async def send_message(message: types.message):
    response = openai.Completion.create(
    model=settings.model,
    prompt=message.text,
    temperature=settings.temperature,
    max_tokens=settings.max_tokens,
    top_p=settings.top_p,
    frequency_penalty=settings.frequency_penalty,
    presence_penalty=settings.presence_penalty)
    print(response['choices'][0]['text'])
    await bot.send_message(message.chat.id, response['choices'][0]['text'])

executor.start_polling(dp)