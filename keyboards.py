from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime
time_zone_keyboard = InlineKeyboardMarkup()
time_zone_keyboard.add(InlineKeyboardButton(
    text="Добавить лекарство",
    callback_data="Добавить лекарство"
))

choose_time_zone_keyboard = InlineKeyboardMarkup(row_width=1)
choose_time_zone_keyboard.add(*[
    InlineKeyboardButton(
        text="America/New_York (UTC +8)",
        callback_data="America/New_York"),
    InlineKeyboardButton(
        text="Indian/Antananarivo (UTC +5:30)",
        callback_data="Indian/Antananarivo"),
    InlineKeyboardButton(
        text="Europe/Moscow (UTC +3)",
        callback_data="Europe/Moscow")
]
)

adding_cure_keyboard = InlineKeyboardMarkup(row_width=1)
adding_cure_keyboard.add(*[
    InlineKeyboardButton(
        text="До недели",
        callback_data="До недели"),
    InlineKeyboardButton(
        text="От 1 недели до месяца",
        callback_data="От 1 недели до месяца"),
    InlineKeyboardButton(
        text="От 1 месяца до года",
        callback_data="От 1 месяца до года"),
    InlineKeyboardButton(
        text="Всегда",
        callback_data="Всегда"),
    InlineKeyboardButton(
        text="Назад 🔙",
        callback_data="adding_cure_back")
]
)

days_of_takeCure_keyboard = InlineKeyboardMarkup()
days_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text="1 день" if i == 1 else i,
    callback_data="days_1 день" if i == 1 else f"days_{i}") for i in range(1, 5)]
)
days_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text=i,
    callback_data=f"days_{i}") for i in range(5, 8)]
)
days_of_takeCure_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="daysWeeksMonths_of_takeCure_back"))

weeks_of_takeCure_keyboard = InlineKeyboardMarkup(row_width=1)
weeks_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text="1 неделю" if i == 1 else i,
    callback_data="weeks_1 неделю" if i == 1 else f"weeks_{i}") for i in range(1, 5)]
)
weeks_of_takeCure_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="daysWeeksMonths_of_takeCure_back"))

months_of_takeCure_keyboard = InlineKeyboardMarkup(row_width=4)
months_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text="1 месяц" if i == 1 else i,
    callback_data="months_1 месяц" if i == 1 else f"months_{i}") for i in range(1, 5)]
)
months_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text=i,
    callback_data=f"months_{i}") for i in range(5, 9)]
)
months_of_takeCure_keyboard.row(*[InlineKeyboardButton(
    text=i,
    callback_data=f"months_{i}") for i in range(9, 12)]
)
months_of_takeCure_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="daysWeeksMonths_of_takeCure_back"))

periodicity_of_takeCure_keyboard = InlineKeyboardMarkup(row_width=1)
periodicity_of_takeCure_keyboard.add(*[
    InlineKeyboardButton(
        text="Несколько раз в день",
        callback_data="Несколько раз в день"),
    InlineKeyboardButton(
        text="1 раз в день",
        callback_data="1 раз в день"),
    InlineKeyboardButton(
        text="1 раз в несколько дней",
        callback_data="1 раз в несколько дней"),
    InlineKeyboardButton(
        text="1 раз в месяц",
        callback_data="1 раз в месяц"),
    InlineKeyboardButton(
        text="Назад 🔙",
        callback_data="periodicity_of_takeCure_back")
]
)

amountTimes_forDay_takeCure_keyboard = InlineKeyboardMarkup()
amountTimes_forDay_takeCure_keyboard.row(*[InlineKeyboardButton(
    text=i,
    callback_data=f"amountTimes_{i}") for i in range(2, 6)]
)
amountTimes_forDay_takeCure_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="amountTimes_forDay_takeCure_back"))

amountDays_forMonth_takeCure_keyboard = InlineKeyboardMarkup()
for j in range(0, 6):
    amountDays_forMonth_takeCure_keyboard.row(*[InlineKeyboardButton(
        text=i,
        callback_data=f"amountDays_{i}") for i in range(2 + (5 * j), 7 + (5 * j))]
    )
amountDays_forMonth_takeCure_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="amountDays_forMonth_takeCure_back"))

cure_time_reception_keyboard = InlineKeyboardMarkup()
timeobj = datetime.timedelta(hours=5, minutes=30)
row_var = 0
for j in range(1, 9):
    cure_time_reception_keyboard.row(*[InlineKeyboardButton(
        text=((str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))
              [0:4] if row_var == 0 else str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[0:5])
              if str(timeobj + datetime.timedelta(minutes=30 * (i + row_var))) not in ["9:00:00", "9:30:00"] else str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[0:4])
        if row_var < 36 else str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[7:][0:4],
        callback_data="cure_time_reception_" + ((str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))
                                                 [0:4] if row_var == 0 else str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[0:5])
                                                if str(timeobj + datetime.timedelta(minutes=30 * (i + row_var))) not in ["9:00:00", "9:30:00"] else str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[0:4])
        if row_var < 36 else "cure_time_reception_" + str(timeobj + datetime.timedelta(minutes=30 * (i + row_var)))[7:][0:4]) for i in range(1, 7)]
    )
    row_var += 6
cure_time_reception_keyboard.row(InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="back_cure_time_reception"))

confirm_keyboard = InlineKeyboardMarkup(row_width=1)
confirm_keyboard.add(*[
    InlineKeyboardButton(
        text="Исправить название",
        callback_data="Исправить название"),
    InlineKeyboardButton(
        text="Изменить длительность",
        callback_data="Изменить длительность"),
    InlineKeyboardButton(
        text="Изменить периодичность",
        callback_data="Изменить периодичность"),
    InlineKeyboardButton(
        text="Изменить время",
        callback_data="Изменить время"),
    InlineKeyboardButton(
        text="ПОДТВЕРДИТЬ",
        callback_data="ПОДТВЕРДИТЬ"),
    InlineKeyboardButton(
        text="Назад 🔙",
        callback_data="confirm_back")
]
)

edit_keyboard = InlineKeyboardMarkup(row_width=1)
edit_keyboard.add(*[
    InlineKeyboardButton(
        text="Исправить название",
        callback_data="Исправить название"),
    InlineKeyboardButton(
        text="Изменить длительность",
        callback_data="Изменить длительность"),
    InlineKeyboardButton(
        text="Изменить периодичность",
        callback_data="Изменить периодичность"),
    InlineKeyboardButton(
        text="Изменить время",
        callback_data="Изменить время"),
    InlineKeyboardButton(
        text="ПОДТВЕРДИТЬ",
        callback_data="ПОДТВЕРДИТЬ"),
    InlineKeyboardButton(
        text="Удаление лекарства",
        callback_data="Удаление лекарства"),
    InlineKeyboardButton(
        text="Назад 🔙",
        callback_data="confirm_back")
]
)

accept_keyboard = InlineKeyboardMarkup()
accept_keyboard.add(InlineKeyboardButton(
    text="Принято",
    callback_data="Принято"
))
