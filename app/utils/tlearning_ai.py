import os
import openai


openai.api_key = "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"

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
    
