import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7635334895:AAET9udMF3im-hdsxuocP3rpE54xFPbhHxc"

CHERNOBYL_PHOTOS = [
    "https://assets3.cbsnewsstatic.com/hub/i/r/2019/05/31/534755e0-1f68-4c7e-bae6-e29ab75f6f50/thumbnail/620x608/36df567da8f3e4de5c4bad67bcc4e95e/burning.jpg?v=45a15310810b79948c864f87b07fc8a0",  # Замените на реальные URL
    "https://assets3.cbsnewsstatic.com/hub/i/r/2019/05/30/82a8b16e-be00-48bb-b6bf-5bc248dc4b71/thumbnail/620x412/ba3b37c1a1c8f4b6d2849d9daa435ef4/gettyimages-57392087.jpg?v=45a15310810b79948c864f87b07fc8a0",
    "https://assets1.cbsnewsstatic.com/hub/i/r/2019/05/31/42182c3e-ec26-4023-9b0b-874b4bd54f75/thumbnail/620x412/6801702e7ce63dce004d4e10924da579/emtombment.jpg?v=45a15310810b79948c864f87b07fc8a0"
]


def get_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("💥 Время взрыва"), KeyboardButton("💂 Какие спец юниты использовались")],
            [KeyboardButton("🏙 Исход города"), KeyboardButton("💀 Смерти")],
            [KeyboardButton("🌆 Что происходит сейчас"), KeyboardButton("☢ Уровень радиации")],
            [KeyboardButton("📞 Связь"), KeyboardButton("📸 Фото ЧАЭС")],
            [KeyboardButton("ℹ Помощь")]
        ],
        resize_keyboard=True
    )


async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}! Я бот и я расскажу тебе всю интересующую информацию о взрыве ЧАЭС.\n"
        "Выбери нужную кнопку ниже:",
        reply_markup=get_keyboard()
    )


async def time(update: Update, context: CallbackContext):
    time_blowing = (
        "💥 Авария на Чернобыльской атомной электростанции (ЧАЭС) произошла в ночь с 25 на 26 апреля 1986 года. "
        "Это крупнейшая катастрофа в атомной энергетике.\n\n"
        "В 01:23:47 (по московскому времени) на 4-м энергоблоке ЧАЭС произошёл взрыв, который полностью разрушил реактор."
    )
    await update.message.reply_text(time_blowing)


async def specop(update: Update, context: CallbackContext):
    spec = (
        "💂 Какие спецподразделения участвовали:\n\n"
        "🎖 1. КГБ СССР (Комитет государственной безопасности):\n"
        "- Расследовали причины аварии\n"
        "- Контролировали информационную блокаду\n"
        "- Отслеживали неблагонадёжных среди ликвидаторов\n\n"
        "🎖 2. МВД СССР (Министерство внутренних дел):\n"
        "- Обеспечивали эвакуацию населения (47 тыс. человек за 36 часов)\n"
        "- Контролировали 30-километровую зону отчуждения\n\n"
        "🎖 3. Советская армия и войска химзащиты:\n"
        "- 340 тыс. военнослужащих участвовали в ликвидации\n"
        "- Вертолётчики сбрасывали свинец и доломит в реактор\n\n"
        "🎖 4. 7-е управление КГБ (специальная разведка):\n"
        "- Собирали образцы грунта и воды в зоне поражения\n\n"
        "🎖 5. ГРУ Генштаба (военная разведка):\n"
        "- Анализировали международную реакцию\n\n"
        "🎖 6. Главное управление лагерей (ГУЛАГ):\n"
        "- Заключённые участвовали в особо опасных работах"
    )
    await update.message.reply_text(spec)


async def exodus(update: Update, context: CallbackContext):
    cities = (
        "🏙 Исход города:\n\n"
        "Сегодня Припять - это город-призрак, расположенный в Чернобыльской зоне отчуждения.\n\n"
        "Он стал своеобразным музеем под открытым небом и памятником крупнейшей техногенной катастрофы в истории.\n\n"
        "До начала полномасштабной войны в Украине Припять была популярным местом для туристов со всего мира.\n\n"
        "Атмосфера заброшенного города вдохновила создателей знаменитой украинской компьютерной игры S.T.A.L.K.E.R."
    )
    await update.message.reply_text(cities)


async def deathing(update: Update, context: CallbackContext):
    death = (
        "💀 Количество жертв:\n\n"
        "Точное количество пострадавших от чернобыльской аварии определить невозможно.\n\n"
        "По разным данным:\n"
        "- Непосредственно от аварии погибло до 50 человек\n"
        "- В первые три месяца скончалось 30 человек\n"
        "- С 1987 по 2004 год ещё 19 смертей можно отнести к её прямым последствиям"
    )
    await update.message.reply_text(death)


async def now(update: Update, context: CallbackContext):
    today = (
        "🌆 Текущая ситуация:\n\n"
        "В настоящее время ведутся работы по выводу из эксплуатации АЭС и преобразованию разрушенного "
        "в результате аварии четвёртого энергоблока в экологически безопасную систему.\n\n"
        "Полный вывод из эксплуатации запланирован к 2065 году."
    )
    await update.message.reply_text(today)


async def radiation(update: Update, context: CallbackContext):
    rad = (
        "☢ Уровень радиации при взрыве:\n\n"
        "При взрыве 4-го реактора Чернобыльской атомной электростанции "
        "26 апреля 1986 года уровень радиации в наиболее пострадавших зонах здания реактора, "
        "по оценкам, составлял 5,6 рентгена в секунду, что эквивалентно более чем 20 000 рентген в час."
    )
    await update.message.reply_text(rad)


async def contact(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📞 Связь с разработчиком:\n\n"
        "По всем вопросам пишите мне в Telegram: @lKiraSl\n\n"
        "Я отвечу вам как можно скорее!"
    )


async def send_photos(update: Update, context: CallbackContext):
    try:
        caption = "📸 Фотографии аварии на Чернобыльской АЭС (26 апреля 1986 года)"
        await update.message.reply_photo(
            photo=CHERNOBYL_PHOTOS[0],
            caption=caption
        )

        for photo_url in CHERNOBYL_PHOTOS[1:]:
            await update.message.reply_photo(photo=photo_url)

    except Exception as e:
        logger.error(f"Ошибка при отправке фотографий: {e}")
        await update.message.reply_text("⚠ Не удалось загрузить фотографии. Попробуйте позже.")


async def help_command(update: Update, context: CallbackContext):
    help_text = (
        "ℹ Доступные функции:\n\n"
        "💥 Время взрыва - Когда произошла авария\n"
        "💂 Спецподразделения - Какие силы участвовали\n"
        "🏙 Исход города - Что стало с Припятью\n"
        "💀 Смерти - Количество жертв аварии\n"
        "🌆 Что сейчас - Текущее состояние ЧАЭС\n"
        "☢ Радиация - Уровни радиации при взрыве\n"
        "📞 Связь - Контакты разработчика\n"
        "📸 Фото ЧАЭС - Фотографии аварии"
    )
    await update.message.reply_text(help_text)


async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "💥 Время взрыва":
        await time(update, context)
    elif text == "💂 Какие спец юниты использовались":
        await specop(update, context)
    elif text == "🏙 Исход города":
        await exodus(update, context)
    elif text == "💀 Смерти":
        await deathing(update, context)
    elif text == "🌆 Что происходит сейчас":
        await now(update, context)
    elif text == "☢ Уровень радиации":
        await radiation(update, context)
    elif text == "📞 Связь":
        await contact(update, context)
    elif text == "📸 Фото ЧАЭС":
        await send_photos(update, context)
    elif text == "ℹ Помощь":
        await help_command(update, context)
    else:
        await update.message.reply_text("Используйте кнопки для навигации", reply_markup=get_keyboard())


async def error_handler(update: object, context: CallbackContext):
    logger.error("Exception while handling an update:", exc_info=context.error)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
