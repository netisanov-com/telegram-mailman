import logging
import os

import requests
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    chat_id: str
    text: str


@app.post('/send_message')
async def send_message(data: Data):
    try:
        url = f"https://api.telegram.org/bot{os.getenv('BOT_API_TOKEN')}/sendMessage"
        response = requests.post(url, data.dict())
        if response.status_code == 200:
            return Response(status_code=200)
        logging.error(msg=f"External Error: Code: {response.status_code}, Data: {response.text}")
        return Response(status_code=500)
    except Exception as e:
        logging.error(msg=f"Internal Error", exc_info=e.__traceback__)
        return Response(status_code=500)


