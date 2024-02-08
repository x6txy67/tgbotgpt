from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

first_keyboard = InlineKeyboardMarkup()
first_keyboard.add(InlineKeyboardButton("A. Сохранение капитала", callback_data="answer_1"))
first_keyboard.add(InlineKeyboardButton("B. Доход", callback_data="answer_2"))
first_keyboard.add(InlineKeyboardButton("C. Рост", callback_data="answer_3"))
first_keyboard.add(InlineKeyboardButton("D. Спекуляция", callback_data="answer_4"))


questions = {
    "2. Инвестиционный горизонт:": [
        "answer_1 A. Менее 1 года",
        "answer_2 B. 1-3 года",
        "answer_3 C. 3-5 лет",
        "answer_4 D. Более 5 лет",
    ],
    "3. Толерантность к риску:": [
        "answer_1 A. Продать все инвестиции",
        "answer_2 B. Продать некоторые инвестиции",
        "answer_3 C. Ничего не делать",
        "answer_4 D. Покупать больше инвестиций",
    ],
    "4. Стабильность доходов:":[
        "answer_1 A. Совсем не стабильно",
        "answer_2 B. Отчасти стабильно",
        "answer_3 C. Стабильно",
        "answer_4 D. Очень стабильно",
    ],
    "5. Финансовые знания:": [
        "answer_1 A. Новичок",
        "answer_2 B. Средний",
        "answer_3 C. Продвинутый",
        "answer_4 D. Эксперт",
    ],
    "6. Резервный фонд:": [
        "answer_1 A. Нет",
        "answer_2 B. Да",
    ],
    "7. Инвестиционный опыт:": [
        "answer_1 A. Нету",
        "answer_2 B. Немного опытный",
        "answer_3 C. Опытный",
        "answer_4 D. Очень опытный",
    ],
}
