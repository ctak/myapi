from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.question import question_router
from domain.answer import answer_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#   return { "message": "안녕하세요 파이보" }

app.include_router(question_router.router)
app.include_router(answer_router.router)
