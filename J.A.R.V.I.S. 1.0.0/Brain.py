# Brain
# Uses LLM to classify/interprete user input and chooses appropriate response/action
import LLM_interface
import command_interface
import log
import info_interface
import personality

class cortex():
    def __init__(self):
        None
    
    def interpret_prompt_completion(self, prompt):
        primer = "You are an AI that classifies prompts from a user. If the prompt requires current information to answer, respond only with REQUEST. If the prompt contains an instruction, respond only with COMMAND. if the prompt does not fall in either catagory, respond only with NORMAL.\n USER: dim the lights\nAI:COMMAND\nUSER:what time is it\nAI:REQUEST\nUSER:Hey buddy\nAI:NORMAL\nUSER:"
        classifier= LLM_interface.prompt_LLM(prompt, primer)
        log.log("Prompt classifier", classifier)
        if "COMMAND" in classifier:
            self.interpret_command(prompt)
        if "REQUEST" in classifier:
            self.interpret_request(prompt)
        if "NORMAL" in classifier:
            None # interact

    def interpret_prompt(self, prompt):
        classifier = LLM_interface.chat_LLM(system_message="You are an AI that classifies prompts from a user. If the prompt requires current information to answer, respond only with REQUEST. If the prompt contains an instruction, respond only with COMMAND. if the prompt does not fall in either catagory, respond only with NORMAL.")
        primers = {
        "dim the lights": "COMMAND",
        "what time is it": "REQUEST",
        "Hey buddy": "NORMAL"
        }
        classifier.load_primers(primers)
        type = classifier.prompt(prompt)
        if "COMMAND" in type:
            self.interpret_command(prompt)
        if "REQUEST" in type:
            self.interpret_request(prompt)
        if "NORMAL" in type:
            None # interact
        
    def interpret_command(self, prompt):
        cmd_interpretor = LLM_interface.chat_LLM(system_message="You are an AI that detects a user's intent and selects the appropriate command and parameters to the command. These are available commands. if the users statement implies they would like an action to be completed, choose the appropriate command:\n\nCommands\nLIGHTS 'Level' - sets the lights to a certain level of brightness between 0 and 10\nOPENFILE 'filename' - opens a file called file name\nCLOSEFILE 'filename' - closes a file called file name\n\nCOMPUTER 'state' - turns the computer on if state=ON and off if state=OFF")
        primers = {
        "Im going to sleep": "LIGHTS '0'",
        "im leaving the room, turn everything off": "LIGHTS '0', COMPUTER 'OFF'",
        "set up my workspace": "LIGHTS '10', COMPUTER 'ON'",
        "open my school file": "OPENFILE 'school'",
        "shut everything down": "LIGHTS '0', COMPUTER 'OFF'"
        }
        cmd_interpretor.load_primers(primers)
        log.log("Chat history", cmd_interpretor.chat_history)
        command = cmd_interpretor.prompt(prompt)
        log.log("Interpreting command", f"Command: <{prompt}> Interpretation: <{command}>")
        command_interface.execute_command(command)
            

    def interpret_request():
        None
    
