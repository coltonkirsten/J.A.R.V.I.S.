# Command Interface
# Allows Jarvis to execute commands
import re
import govee_interface

def isolate_numbers(s):
    return re.findall(r'\d+', s)

def execute_command(command):
    if "LIGHTS" in command:
        brightness = isolate_numbers(command)[0]
        govee_interface.light_control(int(brightness))
