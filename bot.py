import asyncio
import os
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest

logging.basicConfig(level=logging.INFO)

TOKEN = "9087465860:AAFLeVGiQAsWGsV4DnLpK-qzuxPWzMdvy80"
ADMIN_ID = 8739974127
ADMIN_USERNAME = "https://t.me/btrgamingzone"
UPI_ID = "Q378575515@ybl"
QR_PHOTO_ID = "AgACAgUAAxkBAAOaauT47Mgy69bhoZGOjgKg-HMvtvYAAoUTaxuIOilXbImP-hWXZ9gBAAMCAAN4AAM9BA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💵 ₹700 बजट की IDs", callback_data="budget_700"),
         InlineKeyboardButton(text="💵 ₹1500 बजट की IDs", callback_data="budget_1500")],
        [InlineKeyboardButton(text="💵 ₹3500 बजट की IDs", callback_data="budget_3500"),
         InlineKeyboardButton(text="💵 ₹7500 बजट की IDs", callback_data="budget_7500")],
        [InlineKeyboardButton(text="💵 ₹8000 बजट की IDs", callback_data="budget_8000")],
        [InlineKeyboardButton(text="📞 एडमिन से संपर्क करें", url=ADMIN_USERNAME)],
        [InlineKeyboardButton(text="🔄 मुख्य मेनू", callback_data="home")]
    ])

@dp.message(CommandStart())
async def start(m: types.Message):
    try:
        await m.answer(
            "⚡ **BTR GAMING ZONE** ⚡\n🔥 100% भरोसेमंद और सुरक्षित Free Fire ID स्टोर\n\n👇 **अपना बजट चुनें:**",
            reply_markup=get_main_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logging.error(f"Error in start: {e}")

@dp.callback_query(F.data == "home")
async def home(c: types.CallbackQuery):
    try:
        await c.message.edit_text(
            "⚡ **BTR GAMING ZONE** ⚡\n🔥 100% भरोसेमंद और सुरक्षित Free Fire ID स्टोर\n\n👇 **अपना बजट चुनें:**",
            reply_markup=get_main_menu(),
            parse_mode="Markdown"
        )
    except TelegramBadRequest:
        await c.message.answer(
            "⚡ **BTR GAMING ZONE** ⚡\n🔥 100% भरोसेमंद और सुरक्षित Free Fire ID स्टोर\n\n👇 **अपना बजट चुनें:**",
            reply_markup=get_main_menu(),
            parse_mode="Markdown"
        )
    except Exception:
        pass
    await c.answer()

# ==================== BUDGET 700 ====================
@dp.callback_query(F.data == "budget_700")
async def budget_700(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹700 - ID 1", callback_data="id_700_1"),
         InlineKeyboardButton(text="🎮 ₹700 - ID 2", callback_data="id_700_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹700**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except Exception:
        await c.message.answer("💵 **बजट: ₹700**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_700_1")
async def id_700_1(c: types.CallbackQuery):
    await c.answer("लोड हो रहा है...")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_700_1")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_700")]
    ])
    try:
        await c.message.answer("👑 **₹700 - ID 1**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
        p = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIDhGrmWPMp_JHFWO1w9q2C7XBrrK5TAALKGWsbyXEwV8U6q7gemAXlAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDhWrmWPPZvkHTvvNc3Zo1AAG-0tfTcQACyxlrG8lxMFfG3bCZI-wnsgEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDeGrmWOSN0L2lTa7MS7xOXG_nucn7AALGGWsbyXEwV6zxvH1WnsY-AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDcmrmWORkXf6JIJ1oQ77AO7qOEgABQAACwBlrG8lxMFc7nLx_RO3ibQEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDe2rmWOTDb-EKhlCRINtH-y_xmEpWAALJGWsbyXEwVxS0KMP1ppjDAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDdWrmWORjp8f4YygAAbaMpDgx8RRgAQACwxlrG8lxMFf35r4cuPADQQEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDdmrmWOQn7fAKOsE595lgUmkKgjfjAALEGWsbyXEwVx5dqZoKth9SAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDc2rmWOQr46t7xkAl2-yqnwLN8ndQAALBGWsbyXEwVwHovMTuP97vAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDdGrmWOS_3U1B1jOwsvroYtDe7YDlAALCGWsbyXEwV0VbzJ4RLgyGAQADAgADeQADPQQ")
        ]
        await c.message.answer_media_group(media=p)
        await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")

@dp.callback_query(F.data == "id_700_2")
async def id_700_2(c: types.CallbackQuery):
    await c.answer("लोड हो रहा है...")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_700_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_700")]
    ])
    try:
        await c.message.answer("👑 **₹700 - ID 2**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
        p = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIDpmrmW00hQJatVYESuWeTgQUDFQL5AALeGWsbyXEwVzwJnsOk050VAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDoGrmW032Yrh7QeuHm80IPV1F4lU7AALYGWsbyXEwV9eoYXOpCvBTAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDomrmW03DNbTLyMpsOCAH6NiSsl9RAALaGWsbyXEwV6hdPsyKrB3DAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDnmrmW01TA04y0KLH4wayWY7R3bbXAALWGWsbyXEwV_mtzoVyA-ygAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDo2rmW01KJ0Y8nw7XU0gDHb2Bd2LzAALbGWsbyXEwVzrC7sFMO_70AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDn2rmW02UrIcHpgaNwQLyV28z4R5MAALXGWsbyXEwV5vDOCVRz_gLAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDpGrmW017KojeRL5K2S1TaHzl8UkdAALcGWsbyXEwV2JDyahA8dPHAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDpWrmW03hSt1AdkCGz1PyzGJzaxUiAALdGWsbyXEwV9axVfIhm3wVAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDoWrmW03xTGbQR3pSw5QJ8LAUTcWdAALZGWsbyXEwV433ZdvOfJP2AQADAgADeQADPQQ")
        ]
        await c.message.answer_media_group(media=p)
        await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")

# ==================== BUDGET 1500 ====================
@dp.callback_query(F.data == "budget_1500")
async def budget_1500(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text(
            "💵 **बजट: ₹1500**\n\n❌ **All ID sold in this budget, please check other budget IDs.**",
            reply_markup=kb,
            parse_mode="Markdown"
        )
    except Exception:
        await c.message.answer(
            "💵 **बजट: ₹1500**\n\n❌ **All ID sold in this budget, please check other budget IDs.**",
            reply_markup=kb,
            parse_mode="Markdown"
        )
    await c.answer()

# ==================== BUDGET 3500 ====================
@dp.callback_query(F.data == "budget_3500")
async def budget_3500(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹3500 - ID 6", callback_data="id_3500_6")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹3500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except Exception:
        await c.message.answer("💵 **बजट: ₹3500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_6")
async def id_3500_6(c: types.CallbackQuery):
    await c.answer("लोड हो रहा है...")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_6")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    try:
        await c.message.answer("👑 **₹3500 - ID 6**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
        p1 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIDP2rmVnpuFnI65Wr-Li19mZJPq5LWAAKnGWsbyXEwVwhZtZeVZMY5AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDPmrmVnrJWpBlVyv7Z8_EsY9LC7w1AAKmGWsbyXEwV0qbyx44SVvSAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDR2rmVnoIU9bcKbygZZN1XYHjW6_yAAKvGWsbyXEwV1zlVJnw9vgUAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDRmrmVnpABBDCXzLH9vUBvbH0qRDTAAKuGWsbyXEwV-RPdyJu-R5KAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDQmrmVnrBzXYvXEVQj1k1h28uxVOeAAKqGWsbyXEwV0E5Ssp0CeHEAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDRWrmVnoN939uwbSotfICUeDa6Ge5AAKtGWsbyXEwV3KRwnEdunKEAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDRGrmVnrE_Tw9rYm3kKzWL6H8va78AAKsGWsbyXEwV9ULszTKRFHVAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDQ2rmVnpGufTNcjepiB9uLbb8z_k0AAKrGWsbyXEwV26DQ7PFwSNuAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDQWrmVnpfgvhpG2FPc00Sr2Mhdps9AAKpGWsbyXEwV2r9OxrkQfOmAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDQGrmVnqgOs9e2XJLFQPzx0-XTQ1oAAKoGWsbyXEwVw6RkrDP4Pf-AQADAgADeQADPQQ")
        ]
        p2 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIDUmrmVpE9ggXgr2-CzSBUF3HrKF2xAAKwGWsbyXEwVzVxXGEbSbenAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDVWrmVpENc0kYPz0wJLQUI5VN6aX-AAKzGWsbyXEwV8TTCzw7RnDYAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDVmrmVpEEshgwoZ769ZVQ457ZqmRkAAK0GWsbyXEwVw5jXh3ZIHn8AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDVGrmVpFSHZERWDVINXwePoQN1mjpAAKyGWsbyXEwV4ufOT6cs6P6AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIDU2rmVpHmjMvwzZ2oBGekjGSUxRIuAAKxGWsbyXEwVzb4KXy1mOXIAQADAgADeQADPQQ")
        ]
        await c.message.answer_media_group(media=p1)
        await asyncio.sleep(1)
        await c.message.answer_media_group(media=p2)
        await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")

# ==================== BUDGET 7500 ====================
@dp.callback_query(F.data == "budget_7500")
async def budget_7500(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹7500 - ID 2", callback_data="id_7500_2")],
        [InlineKeyboardButton(text="🎮 ₹7500 - ID 3", callback_data="id_7500_3")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹7500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except Exception:
        await c.message.answer("💵 **बजट: ₹7500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_7500_2")
async def id_7500_2(c: types.CallbackQuery):
    await c.answer("लोड हो रहा है...")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_7500_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_7500")]
    ])
    try:
        await c.message.answer("👑 **₹7500 - ID 2**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
        p1 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIBjWrlvKtdeeyhrFwF6LVkL5SEJjNjAALTF2sbiDoxV82vRT9wUoMiAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBjmrlvKsEfotglMyvKAABMIOlyLRTDwAC1BdrG4g6MVfC5LUbj4SBnAEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBiWrlvKuaqj7qj-iysqen3BoZ9bqPAALPF2sbiDoxV9qsboUGYGODAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBi2rlvKuKaoQI76V99MbkQ8KW38h0AALRF2sbiDoxV_NJGCenY99JAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBh2rlvKtoJVWbcWa0q9IAAcOqyflfrAACzRdrG4g6MVfA9Y0lpmMuoAEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBiGrlvKvbuqtO9CJH3RZDX1a8_-TaAALOF2sbiDoxV_OXFZx28ARQAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBhmrlvKsQcxHCM9aeat5mb5SnmhOuAALMF2sbiDoxV-KYjGHdA87HAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBj2rlvKt8Hi9IzJKklS_Ludry37vfAALVF2sbiDoxV8G6xJQkpcijAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBimrlvKuC3p5DBTHqfaqzmxeO7zZfAALQF2sbiDoxV4fLWf0kUqOlAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBjGrlvKu6KHp0z9intOg7ggjFmYCxAALSF2sbiDoxVyLmyOUWQPesAQADAgADeQADPQQ")
        ]
        p2 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIBnWrlvKw1MkkBwDsUKkKJFo2YUFJpAALeF2sbiDoxV-fQf5rZHVvSAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBl2rlvKwhdLcGqa9v05kHMkiDj2HyAALZF2sbiDoxV-R8HFQ1WPeFAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBlWrlvKwTNwhUPuF8Hah35ZaSUvFNAALXF2sbiDoxV4pKnIHJTe5hAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBmWrlvKx8ujIGUHHBegnsC8o6I9PMAALbF2sbiDoxV9JslkbX07pwAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBnGrlvKxUmmaofYJN7SMkmdqqCu0XAALdF2sbiDoxV6l0mx9aPLTFAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBk2rlvKwRIdSxBr5np1oxyFeLbPpBAALWF2sbiDoxV7dJjYp1MFjVAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBm2rlvKwGRO1z8ZkSIjMbEwLdlH2cAALcF2sbiDoxV_EgoREHpqkyAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBmGrlvKyMSHSNm_1dCOXLeKNhzwABGQAC2hdrG4g6MVfK17_quzUEgAEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBlmrlvKwRJBRiqBcmB86EDPIM3v_2AALYF2sbiDoxV6pRX2vSKpFdAQADAgADeQADPQQ")
        ]
        await c.message.answer_media_group(media=p1)
        await asyncio.sleep(1)
        await c.message.answer_media_group(media=p2)
        await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")

@dp.callback_query(F.data == "id_7500_3")
async def id_7500_3(c: types.CallbackQuery):
    await c.answer("लोड हो रहा है...")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_7500_3")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_7500")]
    ])
    try:
        await c.message.answer("👑 **₹7500 - ID 3**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
        p1 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIBaGrlu91GuKXg0dZlFHkXaFesvw85AAK-F2sbiDoxV01lciMNIEm0AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBa2rlu91vJ41tn4TwRCW3WkKY9lQMAALBF2sbiDoxVzV__jgacVleAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBbmrlu92hvtsEMQQgaLqiV5HEfTwjAALEF2sbiDoxV8fziNkdO5YXAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBZmrlu92E7_rnti94bS22SjjXexY_AAK8F2sbiDoxV5Ith4GO7qOBAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBZ2rlu93mmV6Ikbc0ttdQWtMAAa06wQACvRdrG4g6MVdbDUip1aP68gEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBamrlu90Ki-phQsftqeuYUia1CPxjAALAF2sbiDoxV4uag_qq3gXPAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBbWrlu90F9866B0YTLXFTDjAeVVW7AALDF2sbiDoxV99yI0O-4nloAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBaWrlu936ZcNcU_GrlV6PHM2R2hiIAAK_F2sbiDoxV7TEAYG8V1WBAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBcWrlu94N3QABVQqM5r9_9Fih3qJYLAACxhdrG4g6MVeGzumyoYouogEAAwIAA3kAAz0E"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBcGrlu940wGowp3oKN-xHqKd-KZVxAALFF2sbiDoxV5gJBPzsppGEAQADAgADeQADPQQ")
        ]
        p2 = [
            InputMediaPhoto(media="AgACAgUAAxkBAAIBdGrlu94FmDgfsicVqbFxbnJaDhW0AALJF2sbiDoxVyGrvpxXe5O4AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBbGrlu90oE5xXrx-l_2Vzecp7l9PoAALCF2sbiDoxVxTtCcoWiAGKAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBc2rlu94005oU30AH5QmXE5BZSF7GAALIF2sbiDoxV8pJUx4_KF_5AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBcmrlu95Tnj0Dvu2_K62HEuD8lZBhAALHF2sbiDoxVxp53346SlbkAQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBdWrlu971SiTqiB6_r8is7LCh7WSwAALKF2sbiDoxV6oFITAHPPG7AQADAgADeQADPQQ"),
            InputMediaPhoto(media="AgACAgUAAxkBAAIBZWrlu92szSUBxqI7duvJXvfMOYHBAAK7F2sbiDoxVwj3bX27aCh1AQADAgADeQADPQQ")
        ]
        await c.message.answer_media_group(media=p1)
        await asyncio.sleep(1)
        await c.message.answer_media_group(media=p2)
        await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error: {e}")

# ==================== BUDGET 8000 ====================
@dp.callback_query(F.data == "budget_8000")
async def budget_8000(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹8000 - ID 2", callback_data="id_7500_2")],
        [InlineKeyboardButton(text="🎮 ₹8000 - ID 3", callback_data="id_7500_3")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹8000**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except Exception:
        await c.message.answer("💵 **बजट: ₹8000**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

# ==================== PAYMENT & ADMIN WORKFLOW ====================
@dp.callback_query(F.data.startswith("pay_"))
async def pay_handler(c: types.CallbackQuery):
    _, b, i = c.data.split("_")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ मैंने पेमेंट कर दिया है", callback_data=f"paid_{b}_{i}_{c.from_user.id}")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data=f"id_{b}_{i}")]
    ])
    
    notice = (
        f"💳 **SCAN & PAY (₹{b} - ID {i})**\n\n"
        f"📌 **UPI ID (Tap to Copy):**\n`{UPI_ID}`\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚠️ **महत्वपूर्ण सूचना (100% Trusted Work):**\n"
        "हमारी कोई भी Free Fire ID में Bind Email नहीं है और Email ID में Two-Step Verification नहीं है। "
        "इसलिए आप पेमेंट करके Approval मांगेंगे तो जो Email ID और Password आपको मिलेंगे, "
        "उनसे सीधा ID ओपन हो जाएगी। OTP वगैरह का कोई झंझट नहीं है!\n\n"
        f"📞 कोई समस्या आने पर सीधे संपर्क करें: {ADMIN_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👇 **नीचे दिया गया QR Code स्कैन करके पेमेंट करें और स्क्रीनशॉट भेजें:**"
    )
    
    try:
        await c.message.answer(notice, parse_mode="Markdown")
        await c.message.answer_photo(photo=QR_PHOTO_ID)
        await c.message.answer("👇 पेमेंट करने के बाद इस बटन पर क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error in pay_handler: {e}")
    await c.answer()

@dp.callback_query(F.data.startswith("paid_"))
async def paid_handler(c: types.CallbackQuery, bot: Bot):
    _, b, i, uid = c.data.split("_")
    try:
        await c.message.answer(
            "⏳ **पेमेंट रिक्वेस्ट एडमिन के पास भेज दी गई है!**\n\n"
            "कृपया अपनी पेमेंट का **स्क्रीनशॉट** इसी चैट में सेंड कर दें ताकि एडमिन जल्दी अप्रूव कर सके।"
        )
        admin_kb = InlineKeyboardMarkup(inline_keyboard=[
             [InlineKeyboardButton(text="✅ Approve", callback_data=f"app_{uid}"),
                    admin_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅ Approve", callback_data=f"app_{uid}"),
             InlineKeyboardButton(text="❌ Reject", callback_data=f"rej_{uid}")]
        ])
        user_info = f"@{c.from_user.username}" if c.from_user.username else f"User ID: {uid}"
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 **New Payment Request!**\n\n💰 Budget: ₹{b}\n🎮 ID No: {i}\n👤 User: {user_info}\n🆔 ID: `{uid}`",
            reply_markup=admin_kb,
            parse_mode="Markdown"
        )
    except Exception as e:
        logging.error(f"Error in paid_handler: {e}")
    await c.answer()

@dp.callback_query(F.data.startswith("app_"))
async def approve_handler(c: types.CallbackQuery, bot: Bot):
    if c.from_user.id != ADMIN_ID:
        await c.answer("⚠️ सिर्फ एडमिन ही अप्रूव कर सकते हैं!", show_alert=True)
        return
    uid = int(c.data.split("_")[1])
    try:
        await bot.send_message(
            chat_id=uid,
            text=(
                "🎉 **Payment Approved!**\n\n"
                "आपकी पेमेंट वेरीफाई हो चुकी है। बिना OTP के डायरेक्ट लॉगिन करने के लिए डिटेल्स:\n"
                "📧 **Gmail:** Haiabsj8@gamil.com\n"
                "🔑 **Password:** Hakabs78\n\n"
                f"धन्यवाद! किसी भी सहायता के लिए संपर्क करें: {ADMIN_USERNAME}"
            ),
            parse_mode="Markdown"
        )
        await c.message.edit_text("✅ **Successfully Approved & ID Password Sent!**")
    except Exception as e:
        await c.message.answer(f"⚠️ User ko message bhejne me dikkat hui: {e}")
    await c.answer()

@dp.callback_query(F.data.startswith("rej_"))
async def reject_handler(c: types.CallbackQuery, bot: Bot):
    if c.from_user.id != ADMIN_ID:
        await c.answer("⚠️ सिर्फ एडमिन ही रिजेक्ट कर सकते हैं!", show_alert=True)
        return
    uid = int(c.data.split("_")[1])
    try:
        await bot.send_message(
            chat_id=uid,
            text="❌ **Payment Not Received!**\nआपकी पेमेंट वेरीफाई नहीं हो सकी। कृपया एडमिन से संपर्क करें।",
            parse_mode="Markdown"
        )
        await c.message.edit_text("❌ **Payment Rejected!**")
    except Exception:
        pass
    await c.answer()

@dp.message(F.photo)
async def auto_forward_screenshot(message: types.Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        try:
            user_info = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
            await bot.send_photo(
                chat_id=ADMIN_ID,
                photo=message.photo[-1].file_id,
                caption=f"📸 **New Payment Screenshot Received!**\nFrom: {user_info} (`{message.from_user.id}`)",
                parse_mode="Markdown"
            )
            await message.reply("✅ आपका पेमेंट स्क्रीनशॉट एडमिन को भेज दिया गया है! कृपया कुछ मिनट प्रतीक्षा करें।")
        except Exception as e:
            logging.error(f"Error forwarding photo: {e}")

# ==================== RENDER WEB SERVER ====================
async def health_check(request):
    return web.Response(text="Bot is 100% Healthy and Active!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# ==================== MAIN ====================
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await start_web_server()
    print("Store Bot is starting...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
    
