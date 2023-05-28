# Prompt Interpreter
# Uses LLM to classify/interprete user input and chooses appropriate response/action
import LLM_interface
#### EXAMPLE PROMPTS ####
'''
Hey buddy how are you? - normal
good afternoon - normal
what time is it? - request
lights on - command
open a new project file - command

'''
def interpret_prompt(prompt):
    primer = "You are an AI that classifies prompts from a user. If the prompt requires current information to answer, respond only with REQUEST. If the prompt contains an instruction, respond only with COMMAND. if the prompt does not fall in either catagory, respond only with NORMAL.\n USER: dim the lights\nAI:COMMAND\nUSER:what time is it\nAI:REQUEST\nUSER:Hey buddy\nAI:NORMAL\nUSER:"
    classifier= LLM_interface.prompt_LLM(prompt, primer)
    if "COMMAND" in classifier:
        interpret_command(prompt)
    if "REQUEST" in classifier:
        interpret_request(prompt)
    if "NORMAL" in classifier:
        None # interact


def interpret_command():
    None

def interpret_request():
    None

print(interpret_prompt("whats the last thing you remember?"))