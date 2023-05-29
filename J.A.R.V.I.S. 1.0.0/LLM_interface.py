# LLM Interface
# Manages API calls to interchangeable LLMs

import os
import openai
import log
import api_key

openai.api_key = api_key.openai_key

class chat_LLM:
    def __init__(self, system_message="you are a helpful assistent", model="gpt-3.5-turbo"):
        self.system_message = system_message
        self.model = model
        self.chat_history = []
        self.chat_history.append({"role": "system", "content": self.system_message})
    
    def load_primers(self, primers):
        for primer in primers.items(): #{human_says:ai_says, ... }
            self.chat_history.append({"role": "user", "content": primer[0]})
            self.chat_history.append({"role": "assistant", "content": primer[1]})

    def parse_response(self, response):
        return response["choices"][0]["message"]["content"]

    def prompt(self, prompt):
        self.chat_history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(model=self.model,messages=self.chat_history)
        return(self.parse_response(response))
    
    def get_chat_history(self):
        return self.chat_history

    def set_chat_history(self, history):
        self.chat_history = history

def prompt_LLM(prompt,primer="",start="\nAI:",restart="\nUSER:",temp=0.5,max_tok =200,LLM="text-davinci-003"):
    if prompt == None:
        return "ERROR: No prompt given."

    start_sequence = start
    restart_sequence = restart

    response = openai.Completion.create(
    model=LLM,
    prompt=primer + "" + prompt,
    temperature=temp,
    max_tokens=max_tok,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["text"]
