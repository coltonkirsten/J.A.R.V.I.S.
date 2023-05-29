# LLM Interface
# Manages API calls to interchangeable LLMs

import os
import openai
import log
import api_key

openai.api_key = api_key.key

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