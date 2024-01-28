from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

first_keyboard = InlineKeyboardMarkup()
first_keyboard.add(InlineKeyboardButton("A. Capital preservation", callback_data="answer_1"))
first_keyboard.add(InlineKeyboardButton("B. Income", callback_data="answer_2"))
first_keyboard.add(InlineKeyboardButton("C. Growth", callback_data="answer_3"))
first_keyboard.add(InlineKeyboardButton("D. Speculation", callback_data="answer_4"))


questions = {
    "2. Investment Horizon:": [
        "answer_1 A. Less than 1 year",
        "answer_2 B. 1-3 years",
        "answer_3 C. 3-5 years",
        "answer_4 D. More than 5 years",
    ],
    "3. Risk Tolerance:": [
        "answer_1 A. Sell all investments",
        "answer_2 B. Sell some investments",
        "answer_3 C. Do nothing",
        "answer_4 D. Buy more investments",
    ],
    "4. Income Stability: ":[
        "answer_1 A. Not stable at all",
        "answer_2 B. Somewhat stable",
        "answer_3 C. Stable",
        "answer_4 D. Very stable",
    ],
    "5. Financial Knowledge:": [
        "answer_1 A. Beginner",
        "answer_2 B. Intermediate",
        "answer_3 C. Advanced",
        "answer_4 D. Expert",
    ],
    "6. Emergency Fund:": [
        "answer_1 A. No",
        "answer_2 B. Yes",
    ],
    "7. Investment Experience:": [
        "answer_1 A. None",
        "answer_2 B. Some experience",
        "answer_3 C. Experienced",
        "answer_4 D. Very Experience",
    ],
}
