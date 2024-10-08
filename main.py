from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from utils_func import is_link_secue

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.get("/")
def root() -> str:
    return 'Hello'

@app.get("/ping")
def ping() -> dict[str, str]:
    return { 'ping': 'pong' }

@app.post("/check_url")
async def link(request: URLRequest) -> dict[str, Union[str, None]]:

    link = request.url
    secure = 'not-secured'

    # result = is_link_secue(link)
    # print(result)
    # if result is None:
    #     secure = 'secured'

    result = is_link_secue(link)
    print(result)
    if result == 'db fail' or result == 'ssl fail':
        secure = 'not-secured'
    elif result == 'dct secured 80%':
        secure = "partial"
    else:
        secure = 'secured'

    return {
        'is_secured': secure,
        'failed_by': result 
    }


