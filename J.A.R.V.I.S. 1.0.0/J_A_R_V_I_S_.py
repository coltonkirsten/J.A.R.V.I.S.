# J_A_R_V_I_S_
# Just A Rather Very Intelligent System

import Brain
import log
import voice_synth
 
log.start
greeting = "I am online and ready"
log.log("J_A_R_V_I_S_", greeting)
voice_synth.say(greeting)

user = ""
cortex = Brain.cortex()
while True:
    user = input("USER: ")
    if user == "exit":
        break
    log.log("user input", user)
    cortex.interpret_prompt(user)

log.log("J_A_R_V_I_S_", "<end program>")
log.archive_log()
log.clean_log()