# LLM Interface
# Manages API calls to interchangeable LLMs

import os
import openai
import log

openai.api_key = "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"

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

# Example prompt:
'''
print(prompt_LLM(
    "dim the lights", 
    "You are an AI that detects a user's and selects the appropriate command and parameters to the command. \n\nCommands\nLIGHTS 'Level' - sets the lights to a certain level of brightness between 0 and 10\nOPENFILE 'filename' - opens a file called file name\nCLOSEFILE 'filename' - closes a file called file name\nTIME - returns the current time\nCOMPUTER 'state' - turns the computer on if state=ON and off if state=OFF\nSTART 'software'\n\nExample HUMAN: Im going to sleep \nExample AI: LIGHTS '0'\n\nHUMAN: im leaving the room, turn everything off\n\nAI: LIGHTS '0', COMPUTER 'OFF'\nHUMAN:im back\nAI: LIGHTS '10', COMPUTER 'ON'\nHUMAN:what time is it?\n\nAI: TIME\nHUMAN:shut everything down\n\nAI: LIGHTS '0', COMPUTER 'OFF'\nHUMAN:"
))
'''