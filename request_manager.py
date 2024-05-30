import requests
import httpx
from abc import ABC,  abstractmethod
from openai import AsyncOpenAI
import os

#url = "https://api.openai.com/v1/chat/completions"

OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,
    #http_client=httpx.AsyncClient(proxies="http://")
)
   
class request_manager(ABC):
    myModel=""
    def __init__(self) -> None:
        pass
    def set_model(self, theChatModel: str) -> None:
        self.myModel = theChatModel
        
    def get_model(self) -> str:
        return self.myModel
    
    def __bool__(self):
        return bool(self.myModel)