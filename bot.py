import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest

TOKEN = "9087465860:AAE0wPR3sWVDQD20qcqiPBdKACZ8V5MCiOA"
ADMIN_ID = 8739974127
ADMIN_USERNAME = "https://t.me/btrgamingzone"
UPI_ID = "Q378575515@ybl"
QR_PHOTO_ID = "AgACAgUAAxkBAAOaauT47Mgy69bhoZGOjgKg-HMvtvYAAoUTaxuIOilXbImP-hWXZ9gBAAMCAAN4AAM9BA"

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

# --- ₹700 Budget ---
@dp.callback_query(F.data == "budget_700")
async def budget_700(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹700 - ID 1", callback_data="id_700_1"),
         InlineKeyboardButton(text="🎮 ₹700 - ID 2", callback_data="id_700_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹700**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except TelegramBadRequest:
        pass
    await c.answer()

@dp.callback_query(F.data == "id_700_1")
async def id_700_1(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_700_1")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_700")]
    ])
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
    await c.answer()

@dp.callback_query(F.data == "id_700_2")
async def id_700_2(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_700_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_700")]
    ])
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
    await c.answer()

# --- ₹1500 Budget ---
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
    except TelegramBadRequest:
        pass
    await c.answer()

# --- ₹3500 Budget ---
@dp.callback_query(F.data == "budget_3500")
async def budget_3500(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹3500 - ID 1", callback_data="id_3500_1"),
         InlineKeyboardButton(text="🎮 ₹3500 - ID 2", callback_data="id_3500_2")],
        [InlineKeyboardButton(text="🎮 ₹3500 - ID 3", callback_data="id_3500_3"),
         InlineKeyboardButton(text="🎮 ₹3500 - ID 4", callback_data="id_3500_4")],
        [InlineKeyboardButton(text="🎮 ₹3500 - ID 5", callback_data="id_3500_5"),
         InlineKeyboardButton(text="🎮 ₹3500 - ID 6", callback_data="id_3500_6")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹3500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except TelegramBadRequest:
        pass
    await c.answer()

@dp.callback_query(F.data == "id_3500_1")
async def id_3500_1(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_1")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    await c.message.answer("👑 **₹3500 - ID 1**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
    p1 = [
        InputMediaPhoto(media="AgACAgUAAxkBAAID0WrmXwsVx_TqkqF1C7QpmVLMFjv-AAKRFGsbyXE4Vxfa158NlIgDAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID0GrmXwsKNaB61kIPiGhKNx14HijGAAKQFGsbyXE4V0LQUv_KNxoJAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDzGrmXwsKcK8XJNOZdwZhHL1XC6dkAAKMFGsbyXE4VxFQnPDfVulFAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDyGrmXwu-QZ-7dqU8dbjcx8R_TTUCAAKIFGsbyXE4VzHYr8Q0wUiNAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDy2rmXwt-qis4IWELry-9mshlD400AAKLFGsbyXE4V9dOBlQsBnrdAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDzmrmXwucBPsiCTM_Gcuhx_B26FcBAAKOFGsbyXE4V9CBnZq3ysJzAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDzWrmXwuhnzIotP7ObIMRQlxZ8sVfAAKNFGsbyXE4V8uGEj6bCyLPAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDymrmXws4_G3YCWlg7RW91pksDsAJAAKKFGsbyXE4V_sDhk2azoLzAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDyWrmXws_RLGqNSAfGI9xPbVor5wWAAKJFGsbyXE4V66O8AnaX_g3AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDz2rmXwuI1KTqXCw_cI0gy-kk5V4xAAKPFGsbyXE4V5PimiZDE7A1AQADAgADeQADPQQ")
    ]
    p2 = [
        InputMediaPhoto(media="AgACAgUAAxkBAAID3WrmXx1HlYxoxPM2E6OOXOypDmLUAAKTFGsbyXE4V8J12afb13dZAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID4mrmXx0raHm7QtX88aVUt5VueGh3AAKYFGsbyXE4V_zqC0gx_ztmAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID32rmXx21ELnYGAH9q5nEU4sNxr4rAAKVFGsbyXE4Vzp7YzV9X7_uAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID42rmXx06Ntb1I9CMW4AQHD4Gn2LyAAKZFGsbyXE4V-H2OocuM0NNAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID3GrmXx1l3UzXmtuRVjc5ghvHaLhXAAKSFGsbyXE4V4apAwQXlTuFAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID3mrmXx2-Qyy0OIfDfF9EBYs1_3iUAAKUFGsbyXE4V_em1tBobgMoAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID4WrmXx2RSPPjwBG0rvT-yd4pGWArAAKXFGsbyXE4V2DxywWjdxGQAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAID4GrmXx0zS07dx_WrA3C_sOntFRt3AAKWFGsbyXE4V42BtZ9ZSH6BAQADAgADeQADPQQ")
    ]
    await c.message.answer_media_group(media=p1)
    await asyncio.sleep(1)
    await c.message.answer_media_group(media=p2)
    await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_2")
async def id_3500_2(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_2")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    await c.message.answer("👑 **₹3500 - ID 2**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
    p = [
        InputMediaPhoto(media="AgACAgUAAxkBAAIDt2rmXZkUMF_SLcNImoIsKtGcJ6bHAAKCFGsbyXE4VxY-qIB4vzg5AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDtGrmXZkmku0MOp3BcXq-Sf8AAYfZRwACfxRrG8lxOFelnCFcMHFNLAEAAwIAA3kAAz0E"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDtWrmXZmbNk7EVwrjFaUGFtMXTROEAAKAFGsbyXE4V_qyJ-jUYwnpAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDtmrmXZleWaLVlyCORr_bTnF6BJAIAAKBFGsbyXE4V_y00F0fK-5VAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDvGrmXZkIn8TqbGAvg5Nqmyrcehe1AAKHFGsbyXE4Vw5ickZ7zY3MAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDu2rmXZlwyVvMhJCsoFIXQBrOWvd7AAKGFGsbyXE4VyqJjtU31D-7AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDumrmXZmBtvSv1wEObqcLDb5WWU7xAAKFFGsbyXE4V1o82XvtO9ZZAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDuWrmXZlWESO8l412HNZyw_2ihO5lAAKEFGsbyXE4VxZ5LEnsSl_1AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDs2rmXZlG5bHmh7tjvijNpM5PgbfNAAJ-FGsbyXE4VwZ8PdD3P9ClAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDuGrmXZkaBNDlt9xXUJh9nqTnKF_GAAKDFGsbyXE4Vxvfp2EyR9phAQADAgADeQADPQQ")
    ]
    await c.message.answer_media_group(media=p)
    await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_3")
async def id_3500_3(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_3")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    await c.message.answer("👑 **₹3500 - ID 3**\n\n🎥 वीडियो नीचे है:", parse_mode="Markdown")
    await c.message.answer_video(video="BAACAgUAAxkBAAIDsWrmXCZLgfhl4NMPjgeBCVDcgLnGAAKzJQACyXEwV7ImsQl8RQnmPQQ")
    await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_4")
async def id_3500_4(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_4")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    await c.message.answer("👑 **₹3500 - ID 4**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
    p = [
        InputMediaPhoto(media="AgACAgUAAxkBAAIDkGrmWd-U1P7b62V2ajiJL23jXp3ZAALTGWsbyXEwV18lC6t863t-AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDimrmWd-obymt7C_plP7oDaEUhpHAAALNGWsbyXEwV5fQ6Pme2KJgAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDjGrmWd-7vM1SvnO0jene4F5k02xsAALPGWsbyXEwV6H_EhCrqQjsAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDjWrmWd-NX2eQaPIvPbvgwqPa9jlpAALQGWsbyXEwVz5bO_4WmaOGAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDjmrmWd-tRoElGr8kFhl1KQeeVQEgAALRGWsbyXEwV0lkEzaKOgXqAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDkWrmWd93mcBB9oppOJ7bixcOteStAALUGWsbyXEwV61MPl1Y9pr4AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDi2rmWd8NE2vBBaWqSdKvQcILNjfNAALOGWsbyXEwVwKAT0Zd9fOcAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDiWrmWd_A5v4ruHcbl2IDLcpCLsOAAALMGWsbyXEwVxE9MpLzfHO0AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDj2rmWd9xBSj8FtWxQrAM4PbLzFRNAALSGWsbyXEwV2Czsv2FGul2AQADAgADeQADPQQ")
    ]
    await c.message.answer_media_group(media=p)
    await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_5")
async def id_3500_5(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_5")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
    await c.message.answer("👑 **₹3500 - ID 5**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
    p = [
        InputMediaPhoto(media="AgACAgUAAxkBAAIDYmrmWE8wmQl51f3Ig9dyPB9yTLRzAAK7GWsbyXEwV-NkLjlStBEOAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDXmrmWE9FOygQvPWKYAABJzq8hjsprQACtxlrG8lxMFd9wtu5ZTdnaAEAAwIAA3kAAz0E"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDXWrmWE-OSPYdWZcmZmix6Dmu40ONAAK2GWsbyXEwVyeZGK5tZ-T4AQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDZGrmWE-SiN3qGFP6ObLrP8-gaedLAAK9GWsbyXEwV_vkvKT3KaZZAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDYWrmWE8NivPDrSowX_RGzsAQ7XvPAAK6GWsbyXEwV2uZLLtEB-TaAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDY2rmWE_CP06AtxBLfaXJM4jqU2e6AAK8GWsbyXEwV4WTiCQ7E9JWAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDZmrmWE8E0NirojocnBYMFVw_-xQXAAK_GWsbyXEwV1UY3pko-OSgAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDX2rmWE8UEJh8xGWiEc3ZBtyWIIUrAAK4GWsbyXEwV_Wm7_-IFqdhAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDYGrmWE9mveQtbvoBaHQmG4kLSjiuAAK5GWsbyXEwV547cDC8KFjfAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIDZWrmWE-aA9_ixaye7c-pP0zZ7EjxAAK-GWsbyXEwV6Y1nghdFA6sAQADAgADeQADPQQ")
    ]
    await c.message.answer_media_group(media=p)
    await c.message.answer("⚠️ पेमेंट के लिए नीचे क्लिक करें:", reply_markup=kb, parse_mode="Markdown")
    await c.answer()

@dp.callback_query(F.data == "id_3500_6")
async def id_3500_6(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_3500_6")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_3500")]
    ])
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
    await c.answer()

# --- ₹7500 Budget ---
@dp.callback_query(F.data == "budget_7500")
async def budget_7500(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 ₹7500 - ID 1", callback_data="id_7500_1")],
        [InlineKeyboardButton(text="🎮 ₹7500 - ID 2", callback_data="id_7500_2")],
        [InlineKeyboardButton(text="🎮 ₹7500 - ID 3", callback_data="id_7500_3")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="home")]
    ])
    try:
        await c.message.edit_text("💵 **बजट: ₹7500**\n\n👇 ID चुनें:", reply_markup=kb, parse_mode="Markdown")
    except TelegramBadRequest:
        pass
    await c.answer()

@dp.callback_query(F.data == "id_7500_1")
async def id_7500_1(c: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 खरीदें / Buy Now", callback_data="pay_7500_1")],
        [InlineKeyboardButton(text="⬅️ पीछे जाएं", callback_data="budget_7500")]
    ])
    await c.message.answer("👑 **₹7500 - ID 1**\n\n📸 तस्वीरें नीचे हैं:", parse_mode="Markdown")
    photos = [
        InputMediaPhoto(media="AgACAgUAAxkBAAIBtGrlvYrOxn9MyYP8u5UKAQdvUCCpAALnF2sbiDoxV7C1zloNcYBKAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIBr2rlvYq5sNSO18meeLAIQRcAAYKAdgAC4hdrG4g6MVe5XUA9ApeC2AEAAwIAA3kAAz0E"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIBrWrlvYqTtSyRhZUyNMwR8dqb_bdmAALgF2sbiDoxV6EQtMPQye7MAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIBsGrlvYqEN1fPHC47T0hbNX-9cH1bAALjF2sbiDoxV3kqFbdJOUevAQADAgADeQADPQQ"),
        InputMediaPhoto(media="AgACAgUAAxkBAAIBs2rlvYrQ3SrvVP-rR-naq2jvGc8zAALmF2sbiDoxV2Y
