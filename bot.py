import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.exceptions import TelegramBadRequest

TOKEN = "9087465860:AAFLeVGiQAsWGsV4DnLpK-qzuxPWzMdvy80"
ADMIN_ID = 8739974127
ADMIN_USERNAME = "https://t.me/btrgamingzone"
UPI_ID = "0378575515@ybl"
QR_PHOTO_ID = "AgACAgUAAxkBAAOaauT47Mgy69bhoZGOjgKg-HMvtvYAAoUTaxuIOilXbImP-hWXZ9gBAAMCAAN4AAM9BA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 ₹700 बजट की IDs", callback_data="budget_700"),
         InlineKeyboardButton(text="🛒 ₹1500 बजट की IDs", callback_data="budget_1500")],
        [InlineKeyboardButton(text="🛒 ₹3500 बजट की IDs", callback_data="budget_3500"),
         InlineKeyboardButton(text="🛒 ₹7500 बजट की IDs", callback_data="budget_7500")],
        [InlineKeyboardButton(text="🛒 ₹8000 बजट की IDs", callback_data="budget_8000")],
        [InlineKeyboardButton(text="📞 एडमिन से संपर्क करें", url=ADMIN_USERNAME)],
        [InlineKeyboardButton(text="🔄 मुख्य मेनू", callback_data="home")]
    ])

@dp.message(CommandStart())
async def start(m: types.Message):
    await m.answer(
        "⚡ **BTR GAMING ZONE** ⚡\n🔥 100% भरोसेमंद और सुरक्षित Free Fire ID स्टोर\n\n👇 **अपना बजट चुनें:**",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "home")
async def home(c: types.CallbackQuery):
    try:
        await c.message.edit_text(
            "⚡ **BTR GAMING ZONE** ⚡\n🔥 100% भरोसेमंद और सुरक्षित Free Fire ID स्टोर\n\n👇 **अपना बजट चुनें:**",
            reply_markup=get_main_menu(),
            parse_mode="Markdown"
        )
    except TelegramBadRequest:
        pass
    await c.answer()

@dp.callback_query(F.data.startswith("budget_"))
async def budget_handler(c: types.CallbackQuery):
    budget = c.data.split("_")[1]
    text = (
        f"✅ **₹{budget} बजट की IDs**\n\n"
        f"📌 Payment UPI: `{UPI_ID}`\n"
        f"Payment karne ke baad screenshot bhejein.\n"
        f"Admin Support: {ADMIN_USERNAME}"
    )
    back_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Back", callback_data="home")]
    ])
    try:
        await c.message.edit_text(text, reply_markup=back_btn, parse_mode="Markdown")
    except TelegramBadRequest:
        await c.message.answer(text, reply_markup=back_btn, parse_mode="Markdown")
    await c.answer()

# Render Web Service Health Check Server
async def health_check(request):
    return web.Response(text="Bot is Live and Running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await start_web_server()
    print("Store Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
