import os
import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
print
def ai_request(prompt: str = "Cuéntame un chiste sobre organizaciones"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.2,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

response = ai_request()
response = response["choices"][0]["text"]
print(response)