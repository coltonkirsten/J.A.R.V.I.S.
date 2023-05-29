# Voice Synthesizer
# voice synth interface for jarvis
from gtts import gTTS
from playsound import playsound

def say(message):
    if message == None:
        print("error, no message")
        return
    speech = gTTS(message, tld="co.uk")
    speech.save('voice.mp3')
    playsound('voice.mp3')
    return