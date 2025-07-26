
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-your-api-key")

def ask_gpt(question, df):
    prompt = f"Вот таблица данных:\n{df.to_markdown(index=False)}\n\nВопрос: {question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты аналитик данных, помоги пользователю разобраться в таблице."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Ошибка при обращении к GPT: {e}"
