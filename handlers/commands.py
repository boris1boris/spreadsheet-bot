
from aiogram import types, Dispatcher
from services.spreadsheet import SpreadsheetManager
from services.export import export_to_excel
from utils.gpt_helper import ask_gpt
import os

tables = {}

async def start(msg: types.Message):
    await msg.answer("Привет! Я бот для работы с таблицами. Напиши /newtable чтобы начать.")

async def new_table(msg: types.Message):
    user_id = msg.from_user.id
    tables[user_id] = SpreadsheetManager()
    await msg.answer("Новая таблица создана. Добавь строки: /addrow Продукты | 4500 | 24.07")

async def add_row(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in tables:
        await msg.answer("Сначала создай таблицу: /newtable")
        return
    row = msg.text.replace("/addrow", "").strip().split("|")
    tables[user_id].add_row([cell.strip() for cell in row])
    await msg.answer("Строка добавлена!")

async def view_table(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in tables:
        await msg.answer("Таблица не найдена.")
        return
    preview = tables[user_id].to_string()
    await msg.answer(f"Вот текущая таблица:

{preview}")

async def export_table(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in tables:
        await msg.answer("Нет таблицы для экспорта.")
        return
    file_path = f"{user_id}_table.xlsx"
    export_to_excel(tables[user_id], file_path)
    await msg.answer_document(types.InputFile(file_path))
    os.remove(file_path)

async def ask_question(msg: types.Message):
    user_id = msg.from_user.id
    if user_id not in tables:
        await msg.answer("Сначала создай таблицу: /newtable")
        return
    question = msg.text.replace("/ask", "").strip()
    df = tables[user_id].to_dataframe()
    response = ask_gpt(question, df)
    await msg.answer(response)

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(new_table, commands=["newtable"])
    dp.register_message_handler(add_row, commands=["addrow"])
    dp.register_message_handler(view_table, commands=["view"])
    dp.register_message_handler(export_table, commands=["export"])
    dp.register_message_handler(ask_question, commands=["ask"])
