import time
from config import *
from markups import *
from messages import *
from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram.types import InputFile, InputMedia


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, message_greetings_first)
    time.sleep(1.5)
    await bot.send_message(message.from_user.id, message_greetings_second, reply_markup=markup_greetings)
    time.sleep(1.5)
    message_third = await bot.send_message(message.from_user.id, message_greetings_third, parse_mode="Markdown")
    time.sleep(2)
    await message_third.edit_text(message_greetings_fourth, parse_mode="Markdown")


@dp.message_handler(content_types=['text'])
async def message_handler(message: types.Message):
    if message.text == "🌆 Photo":
        await bot.send_photo(message.from_user.id, photo=image_url_1, reply_markup=markup_photo, caption="🏔️ Mountain")
    if message.text == "📜 Data request":
        await bot.send_message(message.from_user.id, message_data, reply_markup=markup_data)


@dp.callback_query_handler(lambda call: True)
async def call_handler(call: types.CallbackQuery, state: FSMContext):
    if call.data == "markup_photo_edit":
        await call.message.edit_media(media=InputMedia(media=InputFile(image_url_2), caption=f"🌅 Lake"))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    
