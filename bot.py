import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest

TOKEN = "9087465860:AAE0wPR3sWVDQD20qcqiPBdKACZ8V5MCiOA"

ADMIN_ID = 8739974127
ADMIN_USERNAME = "https://t.me/btrgamingzone"
UPI_ID = "0378575515@ybl"
QR_PHOTO_ID = "AgACAgUAAxkBAAOaauT47Mgy69bhoZG0jgKg-HMvtvYAAoUTaxuI0ilXbImP-hWXZ9gBAAMCAAN4AAM4BA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 ₹700 बजट की IDs", callback_data="budget_700")],
        [InlineKeyboardButton(text="🛒 ₹1500 बजट की IDs", callback_data="budget_1500")],
        [InlineKeyboardButton(text="🛒 ₹3500 बजट की IDs", callback_data="budget_3500")],
        [InlineKeyboardButton(text="🛒 ₹7500 बजट की IDs", callback_data="budget_7500")],
        [InlineKeyboardButton(text="🛒 ₹8000 बजट की IDs", callback_data="budget_8000")],
        [InlineKeyboardButton(text="📞 एडमिन से संपर्क करें", url=ADMIN_USERNAME)],
        [InlineKeyboardButton(text="🏠 मुख्य मेनू", callback_data="home")]
    ])

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "👋 **Welcome to Free Fire Store Bot!**\n\nNeeche diye gaye options me se apna budget select karein:",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "home")
async def home_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "👋 **Welcome to Free Fire Store Bot!**\n\nNeeche diye gaye options me se apna budget select karein:",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("budget_"))
async def budget_handler(callback: types.CallbackQuery):
    budget = callback.data.split("_")[1]
    text = (
        f"✅ **₹{budget} बजट की IDs**\n\n"
        f"📌 Payment UPI: `{UPI_ID}`\n"
        f"Payment karne ke baad screenshot aur ID details yahan send karein.\n"
        f"Admin Support: {ADMIN_USERNAME}"
    )
    back_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Back", callback_data="home")]
    ])
    try:
        await callback.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")
    except TelegramBadRequest:
        await callback.message.answer(text, reply_markup=back_btn, parse_mode="Markdown")

async def main():
    print("Store Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
