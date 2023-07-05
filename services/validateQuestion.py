import openai
import gradio

openai.api_key_path= "credencialOpenai.txt"

"""in role user, the content is the question, in role system, the content is the answer"""
messages=[
        {"role": "system",
         "content": "Tú eres un psícologo especialista en test vocacionales y harás preguntas y responderás para perfilar a un estudiante de preparatoria."
        }
]
    
"""This function is to answer the question of the user, the question is the parameter of the function."""
def answerQuestion(questionUser):
    messages.append({"role": "user","content": questionUser})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    replay = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant","content": replay})
    return replay

demo = gradio.Interface(
    fn=answerQuestion, 
    inputs="textbox", 
    outputs="textbox", 
    title="Smart Test Careers", 
    description="Este es un chatbot que te ayudará a encontrar tu vocación profesional."
)
demo.launch(share=True)