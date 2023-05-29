# Prompt Interpreter
# Uses LLM to classify/interprete user input and chooses appropriate response/action
import LLM_interface
import command_interface
import info_interface
import personality

def interpret_prompt(prompt):
    primer = "You are an AI that classifies prompts from a user. If the prompt requires current information to answer, respond only with REQUEST. If the prompt contains an instruction, respond only with COMMAND. if the prompt does not fall in either catagory, respond only with NORMAL.\n USER: dim the lights\nAI:COMMAND\nUSER:what time is it\nAI:REQUEST\nUSER:Hey buddy\nAI:NORMAL\nUSER:"
    classifier= LLM_interface.prompt_LLM(prompt, primer)
    if "COMMAND" in classifier:
        interpret_command(prompt)
    if "REQUEST" in classifier:
        interpret_request(prompt)
    if "NORMAL" in classifier:
        None # interact

def interpret_command(prompt):
    primer = "You are an AI that detects a user's and selects the appropriate command and parameters to the command. \n\nCommands\nLIGHTS 'Level' - sets the lights to a certain level of brightness between 0 and 10\nOPENFILE 'filename' - opens a file called file name\nCLOSEFILE 'filename' - closes a file called file name\nTIME - returns the current time\nCOMPUTER 'state' - turns the computer on if state=ON and off if state=OFF\nSTART 'software'\n\nExample HUMAN: Im going to sleep \nExample AI: LIGHTS '0'\n\nHUMAN: im leaving the room, turn everything off\n\nAI: LIGHTS '0', COMPUTER 'OFF'\nHUMAN:im back\nAI: LIGHTS '10', COMPUTER 'ON'\nHUMAN:what time is it?\n\nAI: TIME\nHUMAN:shut everything down\n\nAI: LIGHTS '0', COMPUTER 'OFF'\nHUMAN:"
    command = LLM_interface.prompt_LLM(prompt, primer)
    command_interface.execute_command(command)
        

def interpret_request():
    None
