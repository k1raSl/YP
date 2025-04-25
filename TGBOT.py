import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7635334895:AAET9udMF3im-hdsxuocP3rpE54xFPbhHxc"

def get_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("💥 Время взрыва"), KeyboardButton("💂 Какие спец юниты использовались")],
            [KeyboardButton("🏙 Исход города"), KeyboardButton("💀 Смерти")],
            [KeyboardButton("🌆 Что происходит сейчас"), KeyboardButton("☢ Уровень радиации")],
            [KeyboardButton("🎲 Случайное число"), KeyboardButton("🔄 Сброс")],
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

async def random_number(update: Update, context: CallbackContext):
    num = random.randint(1, 100)
    await update.message.reply_text(f"🎲 Ваше случайное число: {num}")

async def help_command(update: Update, context: CallbackContext):
    help_text = (
        "ℹ Доступные функции:\n\n"
        "💥 Время взрыва - Когда произошла авария\n"
        "💂 Спецподразделения - Какие силы участвовали\n"
        "🏙 Исход города - Что стало с Припятью\n"
        "💀 Смерти - Количество жертв аварии\n"
        "🌆 Что сейчас - Текущее состояние ЧАЭС\n"
        "☢ Радиация - Уровни радиации при взрыве\n"
        "🎲 Случайное число - Генератор чисел\n"
        "🔄 Сброс - Перезапустить бота"
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
    elif text == "🎲 Случайное число":
        await random_number(update, context)
    elif text == "🔄 Сброс":
        await start(update, context)
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
