from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypinyin import pinyin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],  # Разрешенные источники (указывайте адрес вашего фронтенда)
    allow_origins=['https://showchinese.ru'],  # Разрешенные источники (указывайте адрес вашего фронтенда)
    allow_methods=['*'],  # Разрешенные HTTP-методы (в данном случае все)
    allow_headers=['*'],  # Разрешенные HTTP-заголовки (в данном случае все)
    allow_credentials=True,  # Разрешить отправку куки и заголовка авторизации
    expose_headers=['Content-Disposition'],  # Заголовки, которые могут быть доступны клиенту
)

class Body(BaseModel):
    text: str

@app.post('/get_pinyin')
def get_pinyin(body: Body):
    # Генерируем Pinyin с акцентами (тонами)
    pinyin_result = pinyin(body.text)

    return pinyin_result