import openai
import os
import yaml


class ChatGPT:
    def __init__(self):
        with open("conf/openai.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        api_key = config.get("api_key") or None
        self.model = config.get("model") or "gpt-3.5-turbo"
        base_url = config.get("base_url") or "https://api.openai.com/v1"
        self.system_prompt = config.get("system_prompt")
        self.client = openai.OpenAI(api_key=api_key, base_url=base_url)

    def aiimport(self, input):
        # 输入进openai
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": input},
        ]
        response = self.client.chat.completions.create(
            model=self.model, messages=messages, stream=False
        )
        # 输出openai的回答
        return response.choices[0].message.content
