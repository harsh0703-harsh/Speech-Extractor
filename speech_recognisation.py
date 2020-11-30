import pyttsx3

def assistant(text,gender):
    voice_dict={'Male':0,"Female":1}
    code=voice_dict[gender]
    engine=pyttsx3.init()
    engine.setProperty('rate',120)
    engine.setProperty('volume',0.8)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[code].id)
    engine.say(text)
    engine.runAndWait()

