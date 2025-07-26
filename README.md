
# Spreadsheet Telegram Bot

Этот бот позволяет пользователям создавать таблицы прямо в Telegram, добавлять строки, экспортировать в Excel и использовать GPT для анализа данных.

## Команды

- `/start` — приветствие
- `/newtable` — создать новую таблицу
- `/addrow item | amount | date` — добавить строку
- `/view` — просмотреть таблицу
- `/export` — экспорт в Excel
- `/ask question` — задать вопрос GPT по таблице

## Установка

1. Создай `.env` файл с токенами:

```
BOT_TOKEN=your_telegram_token
OPENAI_API_KEY=your_openai_key
```

2. Установи зависимости:

```
pip install -r requirements.txt
```

3. Запусти бота:

```
python main.py
```
