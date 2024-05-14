
import httpx
#import secret

from openai import OpenAI
from openai import AsyncOpenAI
import os

OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    #http_client=httpx.AsyncClient(proxies=secret.proxy_url)
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