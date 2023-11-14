from aiogram.types import Message, CallbackQuery
import logging.handlers
import logging
import os
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
import keyboards
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime
import re
import json
import pytz
import asyncio

# Логирование.
logger = logging.getLogger(__name__)

# Записываем в переменную результат логирования
os.makedirs("Logs", exist_ok=True)

# Cоздаёт все промежуточные каталоги, если они не существуют.
logging.basicConfig(  # Чтобы бот работал успешно, создаём конфиг с базовыми данными для бота
    level=logging.INFO,
    format="[%(levelname)-8s %(asctime)s at           %(funcName)s]: %(message)s",
    datefmt="%d.%d.%Y %H:%M:%S",
    handlers=[logging.handlers.RotatingFileHandler("Logs/     TGBot.log", maxBytes=10485760, backupCount=0), logging.StreamHandler()])


# Создаём Telegram бота и диспетчер
Bot = aiogram.Bot("")
DP = aiogram.Dispatcher(Bot, storage=MemoryStorage())

# Создаём базу данных
conn = sqlite3.connect('GbuzProject_users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
id INT,
time_zone TEXT,
medicines TEXT);""")
asyncio.set_event_loop(asyncio.new_event_loop())
receptionTimeTask = {}
receptionTimeSubTask_loop1 = {}
receptionTimeSubTask_loop2 = {}
receptionTimeSubTask_loop3 = {}
receptionTimeSubTask_loop4 = {}
receptionTimeSubTask_loop5 = {}
TimeTask = {}
TimeSubTask = {}
# Создаём состояния


class UserState(StatesGroup):
    adding_cure = State()
    reception_time_adding = State()
    time_adding = State()


async def receptionTime_send_message_duration(user_id, time_zone, amountTimes_forDay, cure, state, reception_duration, type_duration_reception):

    if reception_duration == "Всегда":
        while True:
            asyncio.create_task(receptionTime_send_message(
                user_id, time_zone, amountTimes_forDay, cure, state))
            await asyncio.sleep(86400)

    if type_duration_reception == "дня/дней":
        if reception_duration == "1 день":
            reception_duration = 1
        reception_duration = int(reception_duration)

    if type_duration_reception == "недели":
        if reception_duration == "1 неделю":
            reception_duration = 1
        reception_duration = int(reception_duration) * 7

    if type_duration_reception == "месяца/месяцев":
        if reception_duration == "1 месяц":
            reception_duration = 1

        reception_duration = int(reception_duration) * 31

    while reception_duration >= 0:
        task = asyncio.create_task(receptionTime_send_message(
            user_id, time_zone, amountTimes_forDay, cure, state))
        reception_duration -= 1
        await asyncio.sleep(86400)
    else:
        task.cancel()


async def receptionTime_send_message(user_id, time_zone, amountTimes_forDay, cure, state):
    global receptionTimeSubTask_loop1
    global receptionTimeSubTask_loop2
    global receptionTimeSubTask_loop3
    global receptionTimeSubTask_loop4
    global receptionTimeSubTask_loop5

    await state.update_data(accept=False)

    async def loop_1():
        data = await state.get_data()
        if len(amountTimes_forDay['1']) == 4:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['1'][0]), minute=int(amountTimes_forDay['1'][1:3]))
        else:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['1'][0:2]), minute=int(amountTimes_forDay['1'][3:5]))

        while True:  # Создаем цикл
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    async def loop_2():
        data = await state.get_data()
        if len(amountTimes_forDay['2']) == 4:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['2'][0]), minute=int(amountTimes_forDay['2'][1:3]))
        else:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['2'][0:2]), minute=int(amountTimes_forDay['2'][3:5]))

        while True:  # Создаем цикл
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    async def loop_3():
        data = await state.get_data()
        if len(amountTimes_forDay['3']) == 4:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['3'][0]), minute=int(amountTimes_forDay['3'][1:3]))
        else:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['3'][0:2]), minute=int(amountTimes_forDay['3'][3:5]))

        while True:  # Создаем цикл
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    async def loop_4():
        data = await state.get_data()
        if len(amountTimes_forDay['4']) == 4:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['4'][0]), minute=int(amountTimes_forDay['4'][1:3]))
        else:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['4'][0:2]), minute=int(amountTimes_forDay['4'][3:5]))

        while True:  # Создаем цикл
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    async def loop_5():
        data = await state.get_data()
        if len(amountTimes_forDay['5']) == 4:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['5'][0]), minute=int(amountTimes_forDay['5'][1:3]))
        else:
            user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
                hour=int(amountTimes_forDay['5'][0:2]), minute=int(amountTimes_forDay['5'][3:5]))

        while True:  # Создаем цикл
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    receptionTimeSubTask_loop1[int(user_id)][cure] = asyncio.get_event_loop(
    ).create_task(loop_1())
    if '2' in amountTimes_forDay:
        receptionTimeSubTask_loop2[int(user_id)][cure] = asyncio.get_event_loop(
        ).create_task(loop_2())
    if '3' in amountTimes_forDay:
        receptionTimeSubTask_loop3[int(
            user_id)][cure] = asyncio.get_event_loop().create_task(loop_3())
    if '4' in amountTimes_forDay:
        receptionTimeSubTask_loop4[int(
            user_id)][cure] = asyncio.get_event_loop().create_task(loop_4())
    if '5' in amountTimes_forDay:
        receptionTimeSubTask_loop5[int(
            user_id)][cure] = asyncio.get_event_loop().create_task(loop_5())


async def time_send_message_duration(user_id, time_zone, time, cure, state, reception_duration, type_duration_reception, periodicity):
    global TimeSubTask

    if reception_duration == "Всегда":
        while True:
            TimeSubTask[int(user_id)][cure] = asyncio.create_task(time_send_message(
                user_id, time_zone, time, cure, state, periodicity))
            await state.update_data(duration=9999)
            await asyncio.sleep(86400)

    if type_duration_reception == "дня/дней":
        if reception_duration == "1 день":
            reception_duration = 1
        reception_duration = int(reception_duration)

    if type_duration_reception == "недели":
        if reception_duration == "1 неделю":
            reception_duration = 1
        reception_duration = int(reception_duration) * 7

    if type_duration_reception == "месяца/месяцев":
        if reception_duration == "1 месяц":
            reception_duration = 1

        reception_duration = int(reception_duration) * 31

    while reception_duration >= 0:
        TimeSubTask[int(user_id)][cure] = asyncio.create_task(time_send_message(
            user_id, time_zone, time, cure, state, periodicity))
        reception_duration -= 1
        await state.update_data(duration=reception_duration)
        await asyncio.sleep(86400)
    else:
        TimeSubTask.cancel()


async def time_send_message(user_id, time_zone, time, cure, state, periodicity):

    await state.update_data(accept=False)

    data = await state.get_data()
    if len(time) == 4:
        user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
            hour=int(time[0]), minute=int(time[2:4]))
    else:
        user_time = datetime.datetime.now(pytz.timezone(time_zone)).replace(
            hour=int(time[0:2]), minute=int(time[3:5]))

    data = await state.get_data()
    if "1 раз в день" in periodicity:
        while data["duration"] >= 0:
            data = await state.get_data()
            now = datetime.datetime.now(pytz.timezone(time_zone))
            if now >= user_time:
                while not data["accept"]:
                    data = await state.get_data()
                    if not data["accept"]:
                        await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                        await asyncio.sleep(300)

                await state.update_data(accept=False)
                break

            await asyncio.sleep(60)

    elif "1 раз в месяц" in periodicity:
        while data["duration"] >= 0:
            while True:
                now = datetime.datetime.now(pytz.timezone(time_zone))
                data = await state.get_data()
                if now >= user_time:
                    while not data["accept"]:
                        data = await state.get_data()
                        if not data["accept"]:
                            await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                            await asyncio.sleep(300)

                    await state.update_data(accept=False)
                    break

                await asyncio.sleep(60)
            await asyncio.sleep(2678000)
    else:
        periodicity = periodicity.split()
        periodicity[3] = int(periodicity[3])
        while data["duration"] > 0:
            while True:
                now = datetime.datetime.now(pytz.timezone(time_zone))
                data = await state.get_data()
                if now >= user_time:
                    while not data["accept"]:
                        data = await state.get_data()
                        if not data["accept"]:
                            await Bot.send_message(user_id, f"Примите {cure}", reply_markup=keyboards.accept_keyboard)
                            await asyncio.sleep(300)

                    await state.update_data(accept=False)
                    break

                await asyncio.sleep(60)
            await asyncio.sleep(86400 * periodicity[3])


# КОГДА ПОЛЬЗОВАТЕЛЬ ПИШЕТ /start
@DP.message_handler(commands=["start"], state="*")
async def start(msg: Message, state: FSMContext):

    if cur.execute(f"SELECT id FROM users WHERE id='{msg.from_user.id}'").fetchone() is None:
        cur.execute(f"INSERT INTO users ('id') VALUES(?)", (msg.from_user.id,))
        conn.commit()
        await msg.answer('Какой ваш часовой пояс?', reply_markup=keyboards.choose_time_zone_keyboard)
    else:
        await msg.answer("Начало работы", reply_markup=keyboards.time_zone_keyboard)
        await state.finish()


# КОГДА ПОЛЬЗОВАТЕЛЬ ПИШЕТ /add_medicine
@DP.message_handler(commands=["add_medicine"])
async def adding_medicine(msg: Message, state: FSMContext):

    await state.finish()
    await msg.answer("Введите название")
    await UserState.adding_cure.set()


# КОГДА ПОЛЬЗОВАТЕЛЬ ПИШЕТ /view_medicines
@DP.message_handler(commands=["view_medicines"])
async def view_medicines(msg: Message):

    if cur.execute(f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone() is None:
        await msg.answer("Ты ещё не добавил лекарств! ❌")
    else:
        medicines = json.loads(cur.execute(
            f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0])
        if medicines:
            keyboard = InlineKeyboardMarkup()
            for i in medicines.keys():
                keyboard.row(InlineKeyboardButton(
                    text=i,
                    callback_data="view_" + str(i))
                )
            await msg.answer("Все твои лекарства:", reply_markup=keyboard)
        else:
            await msg.answer("Ты ещё не добавил лекарств! ❌")


# КОГДА ПОЛЬЗОВАТЕЛЬ ПИШЕТ /edit_medicines
@DP.message_handler(commands=["edit_medicines"])
async def edit_medicines(msg: Message):

    if cur.execute(f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone() is None:
        await msg.answer("Ты ещё не добавил лекарств! ❌")
    else:
        medicines = json.loads(cur.execute(
            f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0])
        keyboard = InlineKeyboardMarkup()
        for i in medicines.keys():
            keyboard.row(InlineKeyboardButton(
                text=i,
                callback_data="edit_" + str(i))
            )
        await msg.answer("Все твои лекарства:", reply_markup=keyboard)


# Когда пользователь нажимает на кнопку
@DP.callback_query_handler(state="*")
async def callback_worker(call: CallbackQuery, state: FSMContext):
    global receptionTimeTask
    global receptionTimeSubTask_loop1
    global receptionTimeSubTask_loop2
    global receptionTimeSubTask_loop3
    global receptionTimeSubTask_loop4
    global receptionTimeSubTask_loop5
    global TimeTask
    global TimeSubTask

    data = await state.get_data()

    if call.data == "Принято":
        await state.update_data(accept=True)
        await call.message.edit_text("Отлично! ✅")

    if call.data in ["America/New_York", "Indian/Antananarivo", "Europe/Moscow"]:
        time_zone = call.data
        cur.execute("UPDATE users SET time_zone = ? WHERE id = ?",
                    (time_zone, call.from_user.id))
        conn.commit()
        await call.message.edit_text(f'Часовой пояс "{time_zone}" выбран! ✅', reply_markup=keyboards.time_zone_keyboard)
        await state.finish()

    if call.data in ["Добавить лекарство", "Исправить название"] or call.data == "adding_cure_back" and "confirm" not in data:
        if call.data != "Исправить название":
            await state.reset_data()
        await call.message.edit_text("Введите название")
        await UserState.adding_cure.set()

    elif call.data == "До недели" or call.data == "periodicity_of_takeCure_back" and data["type_duration_reception"] == "дня/дней" and data["duration_reception"] != "Всегда":
        await state.update_data(type_duration_reception="дня/дней")
        await call.message.edit_text("Сколько ДНЕЙ нужно принимать?", reply_markup=keyboards.days_of_takeCure_keyboard)

    elif call.data == "От 1 недели до месяца" or call.data == "periodicity_of_takeCure_back" and data["type_duration_reception"] == "недели" and data["duration_reception"] != "Всегда":
        await state.update_data(type_duration_reception="недели")
        await call.message.edit_text("Сколько НЕДЕЛЬ нужно принимать?", reply_markup=keyboards.weeks_of_takeCure_keyboard)

    elif call.data == "От 1 месяца до года" or call.data == "periodicity_of_takeCure_back" and data["type_duration_reception"] == "месяца/месяцев" and data["duration_reception"] != "Всегда":
        await state.update_data(type_duration_reception="месяца/месяцев")
        await call.message.edit_text("Сколько МЕСЯЦЕВ нужно принимать?", reply_markup=keyboards.months_of_takeCure_keyboard)

    elif call.data in ["Изменить длительность", "daysWeeksMonths_of_takeCure_back"] or call.data == "periodicity_of_takeCure_back" and "confirm" not in data:
        await call.message.edit_text(f'В течении какого времени нужно принимать "{data["cure"]}"?', reply_markup=keyboards.adding_cure_keyboard)

    elif call.data == "confirm_back" and "edit_cure" not in data and type(data["periodicity"]) == int or call.data.startswith("amountTimes_") and call.data != "amountTimes_forDay_takeCure_back" or call.data == "Изменить время" and type(data["periodicity"]) == int:
        if call.data.startswith("amountTimes_"):
            await state.update_data(periodicity=int(call.data[12:]))

        data = await state.get_data()
        time_reception_keyboard = InlineKeyboardMarkup()
        for i in range(1, int(data["periodicity"]) + 1):
            time_reception_keyboard.add(InlineKeyboardButton(
                text=f"{i}-й приём: ВЫБРАТЬ ВРЕМЯ",
                callback_data=f"receptionTime_{i}")
            )
        time_reception_keyboard.add(*[InlineKeyboardButton(
            text="Готово ✅",
            callback_data="Готово ✅"),
            InlineKeyboardButton(
            text="Назад 🔙",
            callback_data="time_reception_back"
        )])

        if call.data != "Изменить время":
            await state.update_data(reception_time={})
        await call.message.edit_text("ВРЕМЯ ПРИЁМА", reply_markup=time_reception_keyboard)

    elif call.data in ["adding_cure_back", "periodicity_of_takeCure_back"] or call.data.startswith("cure_time_reception_") or call.data == "back_cure_time_reception" and type(data["periodicity"]) == int:
        if "reception_num" in data and len(str(data["periodicity"])) == 1 and call.data != "adding_cure_back":
            reception_num = data["reception_num"]

            if call.data != "back_cure_time_reception":
                if "reception_time" not in data:
                    reception_time = {reception_num: call.data[20:]}
                else:
                    reception_time = dict(list(data["reception_time"].items(
                    )) + list({reception_num: call.data[20:]}.items()))
                await state.update_data(reception_time=reception_time)
                if cur.execute(f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0] is not None:
                    if "edit_cure" in data:
                        medicines = json.loads(cur.execute(
                            f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
                        medicines[data["edit_cure"]][3] = reception_time
                        medicines = json.dumps(medicines)
                        cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                                    (medicines, call.from_user.id))
                        await state.update_data(non_update=True)
            else:
                if "reception_time" not in data:
                    reception_time = {}
                else:
                    reception_time = data["reception_time"]

            time_reception_keyboard = InlineKeyboardMarkup()
            for i in range(1, int(data["periodicity"]) + 1):
                if str(i) not in reception_time.keys():
                    time_reception_keyboard.add(InlineKeyboardButton(
                        text=f"{i}-й приём: ВЫБРАТЬ ВРЕМЯ",
                        callback_data=f"receptionTime_{i}")
                    )
                else:
                    time_reception_keyboard.add(InlineKeyboardButton(
                        text=f"{i}-й приём: {str(reception_time[str(i)])[:4] if len(str(reception_time[str(i)])) == 7 else str(reception_time[str(i)])[:5]}",
                        callback_data=f"receptionTime_{i}")
                    )
            time_reception_keyboard.add(*[InlineKeyboardButton(
                text="Готово ✅",
                callback_data="Готово ✅"),
                InlineKeyboardButton(
                text="Назад 🔙",
                callback_data="time_reception_back"
            )])
            await call.message.edit_text("ВРЕМЯ ПРИЁМА", reply_markup=time_reception_keyboard)
        else:
            if "type_duration_reception" not in data:
                data["type_duration_reception"] = ""

            if "back" not in call.data:
                time = call.data[20:]
                await state.update_data(time=time)
                if cur.execute(f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0] is not None:
                    if "edit_cure" in data:
                        medicines = json.loads(cur.execute(
                            f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
                        medicines[data["edit_cure"]][3] = time
                        medicines = json.dumps(medicines)
                        cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                                    (medicines, call.from_user.id))
                        await state.update_data(non_update=True)

            await state.update_data(confirm=True)
            if "time" not in data:
                await state.update_data(time='')

            data = await state.get_data()
            await call.message.edit_text(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {data["cure"]} \
                                        \nДлительность приёма: {data["duration_reception"]} {data["type_duration_reception"]} \
                                        \nПериодичность: {data["periodicity"]} \
                                        \nВремя: {data["time"]}', reply_markup=keyboards.confirm_keyboard)

    elif call.data in ["1 раз в несколько дней"] or call.data == "back_cure_time_reception" and "дня/дней" in data["periodicity"]:
        await call.message.edit_text("Раз в сколько дней принимать?", reply_markup=keyboards.amountDays_forMonth_takeCure_keyboard)

    elif call.data in ["Всегда", "Изменить периодичность", "amountTimes_forDay_takeCure_back", "back_cure_time_reception", "time_reception_back", "amountDays_forMonth_takeCure_back"] \
            or call.data.startswith("days_") or call.data.startswith("weeks_") or call.data.startswith("months_"):
        if "duration_reception" not in data:
            await state.update_data(duration_reception="")

        data = await state.get_data()
        if not data["duration_reception"] or data["type_duration_reception"] and 'confirm' not in data or call.data in \
            ["Изменить периодичность", "amountTimes_forDay_takeCure_back", "amountDays_forMonth_takeCure_back"] \
            or call.data == "back_cure_time_reception" and "дня/дней" not in data["periodicity"] and "confirm" not in data \
                or call.data == "time_reception_back" and "confirm" not in data:

            if call.data != "Изменить периодичность":
                if call.data == "Всегда":
                    await state.update_data(duration_reception="Всегда")
                    await state.update_data(type_duration_reception="")
                else:
                    await state.update_data(duration_reception=call.data.split("_")[1])
                await state.update_data(periodicity="")

            await call.message.edit_text("ПЕРИОДИЧНОСТЬ ПРИЁМА", reply_markup=keyboards.periodicity_of_takeCure_keyboard)
        else:
            duration_reception = data["duration_reception"]
            type_duration_reception = data["type_duration_reception"]
            if call.data != "time_reception_back":
                if call.data == "Всегда":
                    await state.update_data(duration_reception="Всегда")
                    await state.update_data(type_duration_reception="")
                    duration_reception = "Всегда"
                    type_duration_reception = ""
                else:
                    await state.update_data(duration_reception=call.data.split("_")[1])
                    duration_reception = call.data.split("_")[1]

            if duration_reception in ["1 день", "1 неделю", "1 месяц"]:
                type_duration_reception = ""

            if "reception_time" in data and "1 раз в" not in str(data["periodicity"]):
                reception_time = data["reception_time"]
                await call.message.edit_text(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {data["cure"]} \
                    \nДлительность приёма: {duration_reception} {type_duration_reception} \
                    \nПериодичность: {data["periodicity"]} раза/раз в день \
                    \nВремя: {", ".join([reception_time[i] for i in reception_time.keys()])}', reply_markup=keyboards.confirm_keyboard)
            else:

                await call.message.edit_text(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {data["cure"]} \
                                \nДлительность приёма: {duration_reception} {type_duration_reception} \
                                \nПериодичность: {data["periodicity"]} \
                                \nВремя: {data["time"]}', reply_markup=keyboards.confirm_keyboard)

    elif call.data == "Несколько раз в день" or call.data == "time_reception_back" and "confirm" not in data:
        await state.update_data(reception_time={})
        await call.message.edit_text("Сколько раз в день принимать?", reply_markup=keyboards.amountTimes_forDay_takeCure_keyboard)

    elif call.data in ["1 раз в день", "1 раз в месяц", "Изменить время", "confirm_back"] or call.data.startswith("amountDays_") or call.data.startswith("receptionTime_"):

        if call.data in ["1 раз в день", "1 раз в месяц"]:
            await state.update_data(periodicity=call.data)

        elif call.data.startswith("receptionTime_"):
            if "confirm" in data:
                if data["confirm"]:
                    await state.update_data(confirm=False)
                    await state.update_data(reception_time={})

            await state.update_data(reception_num=call.data[14:])

        elif call.data.startswith("amountDays_"):
            await state.update_data(periodicity=f"1 раз в {call.data[11:]} дня/дней")

        if cur.execute(f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0] is not None:
            if "edit_cure" in data:
                medicines = json.loads(cur.execute(
                    f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
                data = await state.get_data()
                medicines[data["edit_cure"]][2] = data["periodicity"]
                medicines = json.dumps(medicines)
                cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                            (medicines, call.from_user.id))

        if call.data == "confirm_back" and "edit_cure" in data:
            medicines = json.loads(cur.execute(
                f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
            keyboard = InlineKeyboardMarkup()
            for i in medicines.keys():
                keyboard.row(InlineKeyboardButton(
                    text=i,
                    callback_data="edit_" + str(i))
                )
            await call.message.edit_text("Все твои лекарства:", reply_markup=keyboard)
        else:
            time_zone = cur.execute(
                f"SELECT time_zone FROM users WHERE id='{call.from_user.id}'").fetchone()[0]
            await call.message.edit_text(f'ВРЕМЯ ПРИЁМА \n\nВведите время в вашем часовом поясе ({time_zone}). \
                \nВыберите из предложенных вариантов или введите своё. \nНапример, 8:00 или 8 00', reply_markup=keyboards.cure_time_reception_keyboard)

            if call.data.startswith("receptionTime_"):
                await UserState.reception_time_adding.set()
            else:
                await UserState.time_adding.set()

    elif call.data == "Готово ✅":
        reception_time = {}
        if "reception_time" in data:
            reception_time = data["reception_time"]
            if "type_duration_reception" not in data:
                data["type_duration_reception"] = ""

            if len(reception_time.keys()) == int(data["periodicity"]):
                await state.update_data(confirm=True)
                await call.message.edit_text(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {data["cure"]} \
                            \nДлительность приёма: {data["duration_reception"]} {data["type_duration_reception"]} \
                            \nПериодичность: {data["periodicity"]} раза/раз в день \
                            \nВремя: {", ".join([reception_time[i] for i in reception_time.keys()])}', reply_markup=keyboards.confirm_keyboard)
                return

        try:
            time_reception_keyboard = InlineKeyboardMarkup()
            for i in range(1, int(data["periodicity"]) + 1):
                if str(i) not in reception_time.keys():
                    time_reception_keyboard.add(InlineKeyboardButton(
                        text=f"{i}-й приём: ВЫБРАТЬ ВРЕМЯ",
                        callback_data=f"receptionTime_{i}")
                    )
                else:
                    time_reception_keyboard.add(InlineKeyboardButton(
                        text=f"{i}-й приём: {str(reception_time[str(i)])[:4] if len(str(reception_time[str(i)])) == 7 else str(reception_time[str(i)])[:5]}",
                        callback_data=f"receptionTime_{i}")
                    )
            time_reception_keyboard.add(*[InlineKeyboardButton(
                text="Готово ✅",
                callback_data="Готово ✅"),
                InlineKeyboardButton(
                text="Назад 🔙",
                callback_data="time_reception_back"
            )])
            await call.message.edit_text("Вы ещё не заполнили время для всех приёмов! ❌", reply_markup=time_reception_keyboard)
        except:
            pass

    elif call.data == "ПОДТВЕРДИТЬ":

        if "reception_time" in data:
            reception_time = data["reception_time"]
        else:
            time = data["time"]

        if "non_update" not in data:
            if cur.execute(f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0] is not None:
                medicines = json.loads(cur.execute(
                    f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
                cure = {data["cure"]: [data["duration_reception"], data["type_duration_reception"],
                                       data["periodicity"], data["reception_time"] if "reception_time" in data else data["time"]]}

                if "reception_time" in data:
                    reception_time = cure[data["cure"]][3]

                medicines = dict(list(medicines.items()) + list(cure.items()))
                medicines = json.dumps(medicines)
                cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                            (medicines, call.from_user.id))
            else:
                cure = json.dumps({data["cure"]: [data["duration_reception"], data["type_duration_reception"],
                                                  data["periodicity"], data["reception_time"] if "reception_time" in data else data["time"]]})
                cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                            (cure, call.from_user.id))

        conn.commit()
        if "reception_time" in data:
            if "edit_cure" in data:
                if data["edit_cure"] == data["cure"] and receptionTimeTask[call.from_user.id][data["cure"]]:
                    receptionTimeTask[call.from_user.id][data["cure"]].cancel()
                    receptionTimeTask[call.from_user.id][data["cure"]] = None
                    receptionTimeSubTask_loop1[call.from_user.id][data["cure"]].cancel(
                    )
                    receptionTimeSubTask_loop1[call.from_user.id][data["cure"]] = None
                    receptionTimeSubTask_loop2[call.from_user.id][data["cure"]].cancel(
                    )
                    receptionTimeSubTask_loop2[call.from_user.id][data["cure"]] = None

                    if receptionTimeSubTask_loop3[call.from_user.id][data["cure"]]:
                        receptionTimeSubTask_loop3[call.from_user.id][data["cure"]].cancel(
                        )
                        receptionTimeSubTask_loop3[call.from_user.id][data["cure"]] = None

                    if receptionTimeSubTask_loop4[call.from_user.id][data["cure"]]:
                        receptionTimeSubTask_loop4[call.from_user.id][data["cure"]].cancel(
                        )
                        receptionTimeSubTask_loop4[call.from_user.id][data["cure"]] = None

                    if receptionTimeSubTask_loop5[call.from_user.id][data["cure"]]:
                        receptionTimeSubTask_loop5[call.from_user.id][data["cure"]].cancel(
                        )
                        receptionTimeSubTask_loop5[call.from_user.id][data["cure"]] = None

            receptionTimeTask[call.from_user.id][data["cure"]] = asyncio.create_task(receptionTime_send_message_duration(str(call.from_user.id), cur.execute(f"SELECT time_zone FROM users WHERE id='{call.from_user.id}'").fetchone()[0],
                                                                                                                         reception_time, data["cure"], state, data["duration_reception"], data["type_duration_reception"]))
        else:
            if "edit_cure" in data:
                if data["edit_cure"] == data["cure"] and data["cure"] in TimeTask[call.from_user.id]:
                    TimeTask[call.from_user.id][data["cure"]].cancel()
                    TimeTask[call.from_user.id][data["cure"]] = None
                    TimeSubTask[call.from_user.id][data["cure"]].cancel()
                    TimeSubTask[call.from_user.id][data["cure"]] = None

            TimeTask[call.from_user.id][data["cure"]] = asyncio.create_task(time_send_message_duration(str(call.from_user.id), cur.execute(f"SELECT time_zone FROM users WHERE id='{call.from_user.id}'").fetchone()[0],
                                                                                                       time, data["cure"], state, data["duration_reception"], data["type_duration_reception"], data["periodicity"]))

        await call.message.edit_text("Лекарство добавлено")
        await state.reset_state(with_data=False)

    elif cur.execute(f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone() is not None and call.data.startswith("view_") or call.data.startswith("edit_"):
        medicines = json.loads(cur.execute(
            f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
        if call.data.startswith("view_"):
            call.data = call.data[5:]
            if type(medicines[call.data][3]) == dict:
                await call.message.edit_text(f'Лекарство: {call.data} \
                                    \nДлительность приёма: {medicines[call.data][0]} {medicines[call.data][1]} \
                                    \nПериодичность: {medicines[call.data][2]} раза/раз в день \
                                    \nВремя: {", ".join([medicines[call.data][3][i] for i in medicines[call.data][3].keys()])}')
            else:
                await call.message.edit_text(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {call.data} \
                                \nДлительность приёма: {medicines[call.data][0]} {medicines[call.data][1]} \
                                \nПериодичность: {medicines[call.data][2]} \
                                \nВремя: {medicines[call.data][3]}')

        elif call.data.startswith("edit_"):
            call.data = call.data[5:]
            await state.update_data(cure=call.data)
            await state.update_data(duration_reception=medicines[call.data][0])
            await state.update_data(type_duration_reception=medicines[call.data][1])
            await state.update_data(periodicity=medicines[call.data][2])
            await state.update_data(confirm=True)
            await state.update_data(edit_cure=call.data)

            if type(medicines[call.data][3]) == dict:
                await call.message.edit_text(f'Лекарство: {call.data} \
                                    \nДлительность приёма: {medicines[call.data][0]} {medicines[call.data][1]} \
                                    \nПериодичность: {medicines[call.data][2]} раза/раз в день \
                                    \nВремя: {", ".join([medicines[call.data][3][i] for i in medicines[call.data][3].keys()])}', reply_markup=keyboards.edit_keyboard)
            else:
                await state.update_data(time=medicines[call.data][3])
                await call.message.edit_text(f'Лекарство: {call.data} \
                                \nДлительность приёма: {medicines[call.data][0]} {medicines[call.data][1]} \
                                \nПериодичность: {medicines[call.data][2]} \
                                \nВремя: {medicines[call.data][3]}', reply_markup=keyboards.edit_keyboard)

    elif call.data == "Удаление лекарства":
        medicines = json.loads(cur.execute(
            f"SELECT medicines FROM users WHERE id='{call.from_user.id}'").fetchone()[0])
        _ = medicines.pop(data["edit_cure"])
        medicines = json.dumps(medicines)
        cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                    (medicines, call.from_user.id))
        conn.commit()
        if "edit_cure" in data:
            if data["edit_cure"] == data["cure"] and receptionTimeTask[call.from_user.id][data["cure"]]:
                receptionTimeTask[call.from_user.id][data["cure"]].cancel()
                receptionTimeTask[call.from_user.id][data["cure"]] = None
                receptionTimeSubTask_loop1[call.from_user.id][data["cure"]].cancel(
                )
                receptionTimeSubTask_loop1[call.from_user.id][data["cure"]] = None
                receptionTimeSubTask_loop2[call.from_user.id][data["cure"]].cancel(
                )
                receptionTimeSubTask_loop2[call.from_user.id][data["cure"]] = None

                if receptionTimeSubTask_loop3[call.from_user.id][data["cure"]]:
                    receptionTimeSubTask_loop3[call.from_user.id][data["cure"]].cancel(
                    )
                    receptionTimeSubTask_loop3[call.from_user.id][data["cure"]] = None

                if receptionTimeSubTask_loop4[call.from_user.id][data["cure"]]:
                    receptionTimeSubTask_loop4[call.from_user.id][data["cure"]].cancel(
                    )
                    receptionTimeSubTask_loop4[call.from_user.id][data["cure"]] = None

                if receptionTimeSubTask_loop5[call.from_user.id][data["cure"]]:
                    receptionTimeSubTask_loop5[call.from_user.id][data["cure"]].cancel(
                    )
                    receptionTimeSubTask_loop5[call.from_user.id][data["cure"]] = None
            else:
                TimeTask[call.from_user.id][data["cure"]].cancel()
                TimeTask[call.from_user.id][data["cure"]] = None
                TimeSubTask[call.from_user.id][data["cure"]].cancel()
                TimeSubTask[call.from_user.id][data["cure"]] = None

        await call.message.edit_text("Лекарство удалено.")

# Когда появляется состояние с adding_cure


@ DP.message_handler(state=UserState.adding_cure)
async def adding_cure(msg: Message, state: FSMContext):
    global receptionTimeTask
    global receptionTimeSubTask_loop1
    global receptionTimeSubTask_loop2
    global receptionTimeSubTask_loop3
    global receptionTimeSubTask_loop4
    global receptionTimeSubTask_loop5
    global TimeTask
    global TimeSubTask

    data = await state.get_data()
    if "cure" not in data:
        cure = msg.text
        if msg.from_user.id not in receptionTimeTask:
            receptionTimeTask[msg.from_user.id] = {}
            receptionTimeSubTask_loop1[msg.from_user.id] = {}
            receptionTimeSubTask_loop2[msg.from_user.id] = {}
            receptionTimeSubTask_loop3[msg.from_user.id] = {}
            receptionTimeSubTask_loop4[msg.from_user.id] = {}
            receptionTimeSubTask_loop5[msg.from_user.id] = {}
            TimeTask[msg.from_user.id] = {}
            TimeSubTask[msg.from_user.id] = {}

        receptionTimeTask[msg.from_user.id][cure] = None
        receptionTimeSubTask_loop1[msg.from_user.id][cure] = None
        receptionTimeSubTask_loop2[msg.from_user.id][cure] = None
        receptionTimeSubTask_loop3[msg.from_user.id][cure] = None
        receptionTimeSubTask_loop4[msg.from_user.id][cure] = None
        receptionTimeSubTask_loop5[msg.from_user.id][cure] = None
        TimeTask[msg.from_user.id][cure] = None
        TimeSubTask[msg.from_user.id][cure] = None
        await state.update_data(cure=cure)

        await msg.answer(f'В течении какого времени нужно принимать "{cure}"?', reply_markup=keyboards.adding_cure_keyboard)
        await state.reset_state(with_data=False)
    else:
        cure = msg.text
        await state.update_data(cure=cure)

        if cur.execute(f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0] is not None:
            if "edit_cure" in data:
                medicines = json.loads(cur.execute(
                    f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0])
                medicines[cure] = medicines[data["edit_cure"]]
                del medicines[data["edit_cure"]]
                medicines = json.dumps(medicines)
                cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                            (medicines, msg.from_user.id))
                await state.update_data(non_update=True)

        if "reception_time" in data:
            if "type_duration_reception" not in data:
                data["type_duration_reception"] = ""

            reception_time = data["reception_time"]
            await msg.answer(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {cure} \
            \nДлительность приёма: {data["duration_reception"]} {data["type_duration_reception"]} \
            \nПериодичность: {data["periodicity"]} раза/раз в день \
            \nВремя: {", ".join([reception_time[i] for i in reception_time.keys()])}', reply_markup=keyboards.confirm_keyboard)
        else:
            await msg.answer(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {cure} \
                            \nДлительность приёма: {data["duration_reception"]} {data["type_duration_reception"]} \
                            \nПериодичность: {data["periodicity"]} \
                            \nВремя: {data["time"]}', reply_markup=keyboards.confirm_keyboard)


# Когда появляется состояние с reception_time_adding
@ DP.message_handler(state=UserState.reception_time_adding)
async def reception_time_adding(msg: Message, state: FSMContext):
    reception_time = re.split(';|:|\ |\?', msg.text)
    if len(str(reception_time)) == 11:
        reception_time = str(datetime.timedelta(
            hours=int(reception_time[0]), minutes=int(reception_time[1])))[:4]
    else:
        reception_time = str(datetime.timedelta(
            hours=int(reception_time[0]), minutes=int(reception_time[1])))[:5]

    data = await state.get_data()
    reception_num = data["reception_num"]
    if "reception_time" not in data:
        reception_time = {reception_num: reception_time}
    else:
        reception_time = dict(list(data["reception_time"].items(
        )) + list({reception_num: reception_time}.items()))
    await state.update_data(reception_time=reception_time)
    if cur.execute(f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0] is not None:
        if "edit_cure" in data:
            medicines = json.loads(cur.execute(
                f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0])
            medicines[data["edit_cure"]][3] = reception_time
            medicines = json.dumps(medicines)
            cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                        (medicines, msg.from_user.id))
            await state.update_data(non_update=True)

    time_reception_keyboard = InlineKeyboardMarkup()
    for i in range(1, int(data["periodicity"]) + 1):
        if str(i) not in reception_time.keys():
            time_reception_keyboard.add(InlineKeyboardButton(
                text=f"{i}-й приём: ВЫБРАТЬ ВРЕМЯ",
                callback_data=f"receptionTime_{i}")
            )
        else:
            time_reception_keyboard.add(InlineKeyboardButton(
                text=f"{i}-й приём: {str(reception_time[str(i)])}",
                callback_data=f"receptionTime_{i}")
            )

    time_reception_keyboard.add(*[InlineKeyboardButton(
        text="Готово ✅",
        callback_data="Готово ✅"),
        InlineKeyboardButton(
        text="Назад 🔙",
        callback_data="time_reception_back"
    )])
    await msg.answer("ВРЕМЯ ПРИЁМА", reply_markup=time_reception_keyboard)
    await state.reset_state(with_data=False)


# Когда появляется состояние с time_adding
@ DP.message_handler(state=UserState.time_adding)
async def time_adding(msg: Message, state: FSMContext):
    time = re.split(';|:|\ |\?', msg.text)
    if len(str(time)) == 11:
        time = str(datetime.timedelta(
            hours=int(time[0]), minutes=int(time[1])))[:4]
    else:
        time = str(datetime.timedelta(
            hours=int(time[0]), minutes=int(time[1])))[:5]

    await state.update_data(time=time)
    data = await state.get_data()
    if cur.execute(f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0] is not None:
        if "edit_cure" in data:
            medicines = json.loads(cur.execute(
                f"SELECT medicines FROM users WHERE id='{msg.from_user.id}'").fetchone()[0])
            medicines[data["edit_cure"]][3] = time
            medicines = json.dumps(medicines)
            cur.execute("UPDATE users SET medicines = ? WHERE id = ?",
                        (medicines, msg.from_user.id))
            await state.update_data(non_update=True)

    await msg.answer(f'ПОДТВЕРДИТЕ ДОБАВЛЕНИЕ ЛЕКАРСТВА \n\nЛекарство: {data["cure"]} \
                \nДлительность приёма: {data["duration_reception"]} {data["type_duration_reception"]} \
                \nПериодичность: {data["periodicity"]} \
                \nВремя: {data["time"]}', reply_markup=keyboards.confirm_keyboard)
    await state.reset_state(with_data=False)


if __name__ == "__main__":  # Если файл запускается как самостоятельный, а не как модуль
    # В консоле будет отоброжён процесс запуска бота
    logger.info("Запускаю бота...")
    executor.start_polling(  # Бот начинает работать
        dispatcher=DP,  # Передаем в функцию диспетчер
        # (диспетчер отвечает за то, чтобы сообщения пользователя доходили до бота)
        on_startup=logger.info("Загрузился успешно!"), skip_updates=True)
    # Если бот успешно загрузился, то в консоль выведется сообщение
