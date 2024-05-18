
#import secret
#from openai import OpenAI

import requests
import httpx
from openai import AsyncOpenAI
import os

url = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    http_client=httpx.AsyncClient(proxies="http://117.250.3.58:8080")
)
   
class request_manager:
    def __init__(self, theChatModel:str) -> None:
        self.myResponce = ""
        self.myMaxTokens = 100
        self.myChatModel = theChatModel
        self.myTemperature = 0.9
        self.messages = []

    async def send_request(self, theContent:str) -> None:
        self.messages.append({
            "role": "user", 
            "content": theContent
        })
        # headers = {"Content-Type" : "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}" }
        # data = {
        #         "model": "gpt-3.5-turbo",
        #         "messages": [{"role": "user", "content": "Say this is a test!"}],
        #          "temperature": 0.7
        #        }
        # proxies = {
        #             "http" : ""
        #           }
        # aResponce = requests.get(url, headers=headers, data=data, proxies=proxies)
        aResponce = await client.chat.completions.create(
                model = self.myChatModel,
                messages= self.messages,
                max_tokens = self.myMaxTokens,
                temperature = self.myTemperature)
        self.myResponce = aResponce.choices[0].message.content
        self.messages.append({
            "role" : aResponce.choices[0].message.role,
            "content" : self.myResponce
        })
        
    def get_answer(self) -> str:
        if not self.myResponce:
            raise ValueError("Empty answer. Send request first")
        return self.myResponce