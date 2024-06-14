import openai

class ChatGPT:
    def __init__(self, api_key,model="gpt-3.5-turbo",base_url="https://api.openai.com/v1"):
        openai.api_key = api_key
        self.model = model
        openai.base_url = base_url