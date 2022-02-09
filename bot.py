import logging
import wikipedia


from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang("uz")
API_TOKEN = '2105894351:AAFY79SgUGT3_xnYLt9f55ADG7vNYEYoopA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu allaykum!\nXush kelibsiz")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bundaqa maqola topilmadi!")

# url manzil olish
# @dp.message_handler()
# async def echo1(message: types.Message):
#     try:
#         respond = wikipedia.page(message.ny.url)
#         await message.answer(respond)
#     except:
#         await message.answer("Bundaqa url manzil topilmadi!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)