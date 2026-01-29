from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def think(query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, an intelligent assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

