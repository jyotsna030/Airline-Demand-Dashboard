import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_summary(df: pd.DataFrame) -> str:
    data = df.head(10).to_csv(index=False)

    prompt = f"""
    You are a flight data analyst. Based on this airline data, summarize:
    - Popular routes
    - Airlines with many flights
    - Common flight timings (morning/evening etc.)
    - When is demand high and any tips for travelers?

    Data:
    {data}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI Insight Error: {e}"

def answer_user_question(df: pd.DataFrame, question: str) -> str:
    data = df.head(10).to_csv(index=False)

    prompt = f"""
    Here is some airline flight data:
    {data}

    Now answer the question: {question}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Question Answering Error: {e}"
