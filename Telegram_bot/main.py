import asyncio
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart,Command
import os
from dotenv import load_dotenv
from Parsing import  parsing

load_dotenv()


TOKEN = os.getenv('TOKEN_BOT')


bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}, это бот для парсинга данных")

@dp.message(Command('books'))
async def books(message:types.Message):

    await message.answer(f"Вот список книг:")
    data = parsing()
    await message.answer(data, parse_mode="Markdown")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ =="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt :
        print('Бот выключен!')
