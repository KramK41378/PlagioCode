import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def generate_code(prompt):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    response = client.chat.completions.create(
        model="groq/compound",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1024
    )

    code = response.choices[0].message.content.split("\n")
    for line in code:
        if line.lower() == "python" or line == "```" or line.lower() == "```python":
            code.remove(line)
    with open("generated_code.txt", "w") as file:
        for line in code:
            file.write(line)
    return code


if __name__ == "__main__":
    print(generate_code("Напиши код по условию сортировки списка чисел на Python."
                        " Отвечай только кодом без объяснений и комментариев."))
