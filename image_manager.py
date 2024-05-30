
from openai import AsyncOpenAI
from request_manager import request_manager
from request_manager import client

class image_manager(request_manager):
    def __init__(self) -> None:
        self.myResponce = ""
        self.myMaxTokens = 100
        self.myTemperature = 0.9

    async def send_request(self, theContent:str) -> None:
        aResponce = await client.images.generate(
            model=self.myModel,
            prompt=theContent,
            size="256x256",
            quality="standard",
            n=1
        )
        self.myResponce = aResponce.data[0].url
    
    def set_max_tokens (self, theMaxTokens: int) -> None:
        self.myMaxTokens = theMaxTokens
    
    def get_answer(self) -> str:
        if not self.myResponce:
            raise ValueError("Empty answer. Send request first")
        return self.myResponce