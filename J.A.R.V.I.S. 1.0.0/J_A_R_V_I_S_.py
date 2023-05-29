# J_A_R_V_I_S_
# Just A Rather Very Intelligent System

import prompt_interpreter
import log
import voice_synth
 
log.start
log.log("J_A_R_V_I_S_", "J.A.R.V.I.S. is online and ready")
voice_synth.say("I am online and ready")

user = ""
while True:
    user = input("USER: ")
    if user == "exit":
        break
    log.log("user input", user)
    prompt_interpreter.interpret_prompt(user)

log.log("J_A_R_V_I_S_", "J.A.R.V.I.S. terminated")
log.archive_log()
log.clean_log()