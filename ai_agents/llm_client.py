import os


def ask_llm(prompt: str) -> str:
    """
    Ask LLM for a fix suggestion.
    Imported lazily to avoid test-time dependency on OpenAI SDK.
    """
    from openai import OpenAI  # 👈 LAZY IMPORT

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()