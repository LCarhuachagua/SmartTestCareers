from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.validateQuestion import answerQuestion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
def index():
    return {"message": "Working fine"}

@app.post("/welcome-to-chat")
def welcome_chat(name:str):
    return {"message": f"Bienvenido {name}, a tu asesor personalizado para conocer tu perfil vocacional. ¡Empecemos!"}

"""@app.post("/answer-to-question")
def answer_question(questionUser:str):
    chatBotAnswer = answerQuestion(questionUser)
    return {"message": f"Tu respuesta fue {chatBotAnswer}"}"""

