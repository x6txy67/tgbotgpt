import asyncio
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from pymongo import MongoClient

from chatgpt import generate_response

# Load environment variables from .env file
load_dotenv()

# Retrieve the Telegram bot token from the environment variable
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Retrieve MongoDB connection details from the environment variables
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client and connect to the database
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

# Initialize the bot and dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    # Store user information in MongoDB
    user_id = message.from_user.id
    user_paid = False  # You can update this based on whether the user paid or not

    user_data = {
        "_id": user_id,  # Use user_id as the _id field
        "user_paid": user_paid,
    }

    # Insert or update user information in the database
    db.users.update_one({"_id": user_id}, {"$set": user_data}, upsert=True)

    # Reply with a welcome message
    await message.reply("Welcome! You have been added to the database.")


@dp.message_handler()
async def handle_messages(message: types.Message):
    # Send "Loading..." message
    loading_message = await message.reply("Loading...")

    # Generate response using ChatGPT
    prompt = message.text
    response = generate_response(prompt)

    # Simulate processing time (remove in production)
    await asyncio.sleep(2)

    # Edit the loading message with the generated response
    await bot.edit_message_text(
        response, chat_id=loading_message.chat.id, message_id=loading_message.message_id
    )


if __name__ == "__main__":
    # Start the bot
    executor.start_polling(dp, skip_updates=True)
