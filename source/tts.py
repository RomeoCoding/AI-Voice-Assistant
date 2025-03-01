import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed

def speak(text):
    engine.say(text)
    engine.runAndWait()
