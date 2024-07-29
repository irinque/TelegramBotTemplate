from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


markup_greetings = ReplyKeyboardMarkup(resize_keyboard=True)
markup_greetings_photos = KeyboardButton("🌆 Photo")
markup_greetings_requires = KeyboardButton("📜 Data request")
markup_greetings.row(markup_greetings_photos, markup_greetings_requires)

markup_photo = InlineKeyboardMarkup(row_width=1)
markup_photo_edit = InlineKeyboardButton("⚙️ Change", callback_data="markup_photo_edit")
markup_photo_view = InlineKeyboardButton("🔗 Open photo", url="https://img.goodfon.ru/original/1280x1024/0/61/priroda-peyzazh-gora-les.jpg")
markup_photo.row(markup_photo_edit, markup_photo_view)

markup_data = ReplyKeyboardMarkup(resize_keyboard=True)
markup_data_number = KeyboardButton(text="📞 Phone Number", request_contact=True)
markup_data_location = KeyboardButton(text="🌍 Location", request_location=True)
markup_data.row(markup_data_number, markup_data_location)