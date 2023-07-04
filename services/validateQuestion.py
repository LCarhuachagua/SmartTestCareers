import openai
import os

openai.api_key_path= "credencialOpenai.txt"

messages=[
        {"role": "system",
         "content": "Tú eres un psícologo especialista en test vocacionales y harás preguntas y responderás para perfilar a un estudiante de preparatoria."
        }
    ]
    

def answerQuestion(questionUser):
    messages.append({"role": "user","content": questionUser})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    return completion.choices[0].message.content
