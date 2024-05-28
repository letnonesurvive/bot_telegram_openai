import requests
import httpx
from openai import AsyncOpenAI
import os

#url = "https://api.openai.com/v1/chat/completions"

OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,
    #http_client=httpx.AsyncClient(proxies="http://")
)
   
class request_manager:
    def __init__(self, theChatModel:str) -> None:
        self.myResponce = ""
        self.myMaxTokens = 100
        self.myChatModel = theChatModel
        self.myTemperature = 0.9
        self.myMessages = []

    async def send_request(self, theContent:str) -> None:
        self.myMessages.append({
            "role": "user", 
            "content": theContent
        })
        aResponce = await client.chat.completions.create(
                model = self.myChatModel,
                messages= self.myMessages,
                max_tokens = self.myMaxTokens,
                temperature = self.myTemperature)
        self.myResponce = aResponce.choices[0].message.content
        self.myMessages.append({
            "role" : aResponce.choices[0].message.role,
            "content" : self.myResponce
        })
    
    def set_max_tokens (self, theMaxTokens: int) -> None:
        self.myMaxTokens = theMaxTokens
    
    def clear_chat(self):
        self.myMessages.clear()
    
    def get_answer(self) -> str:
        if not self.myResponce:
            raise ValueError("Empty answer. Send request first")
        return self.myResponce
    
    def set_model(self, theChatModel: str) -> None:
        self.myChatModel = theChatModel