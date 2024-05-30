
from openai import AsyncOpenAI
from request_manager import request_manager
from request_manager import client
class chat_manager(request_manager):
    def __init__(self) -> None:
        self.myResponce = ""
        self.myMaxTokens = 100
        self.myTemperature = 0.9
        self.myMessages = []

    async def send_request(self, theContent:str) -> None:
        self.myMessages.append({
            "role": "user", 
            "content": theContent
        })
        aResponce = await client.chat.completions.create(
                model = self.myModel,
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