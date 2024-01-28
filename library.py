import asyncio
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from aiogram.types import ParseMode
from newsmarket import get_market_news
from companynews import get_news
from yf import graph
from yf import news as yf_news
from yf import  get_recommendations_summary
from investgpt import main as testgpt_main
from spheregpt import main as spheregpt_main
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import user
import question as qs
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery