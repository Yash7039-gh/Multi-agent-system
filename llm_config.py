"""
Groq LLM — Direct API (No CrewAI needed)
Works with Python 3.14+
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def get_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "❌ GROQ_API_KEY not found!\n"
            "Please add it to your .env file.\n"
            "Get free key at: https://console.groq.com"
        )
    return Groq(api_key=api_key)


def call_llm(system_prompt: str, user_message: str, temperature: float = 0.7) -> str:
    """Call Groq LLaMA 3 and return the response text."""
    client = get_client()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        temperature=temperature,
        max_tokens=2048,
    )

    return response.choices[0].message.content
