import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5129415684:AAHfrQbaoAe3pLPD8powCR28oswwY3-tk6U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['menu'])
async def echo(message: types.Message):
    kb = types.ReplyKeyboardMarkup().add(types.KeyboardButton('Приложение', web_app=types.web_app_info.WebAppInfo(url='https://google.com')))
    await message.answer(message.text, reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
