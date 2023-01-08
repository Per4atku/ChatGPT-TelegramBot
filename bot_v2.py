import settings
from aiogram import types, executor, Dispatcher, Bot
from pyChatGPT import ChatGPT

api = ChatGPT(settings.CHATGPTTOKEN)
bot = Bot(token=settings.BOTTOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nSend me a request to start")

@dp.message_handler()
async def send_message(message: types.message):
    resp = api.send_message(message.text)
    
    await bot.send_message(message.chat.id, resp['message'])

    api.reset_conversation()  
    api.clear_conversations()  
    api.refresh_chat_page()  


executor.start_polling(dp)