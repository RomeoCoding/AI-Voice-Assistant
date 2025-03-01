# config.py
import openai
WAKE_WORD = "hey assistant"  

SPEECH_RECOGNIZER = "google"  
SPEECH_TIMEOUT = 5  # Max seconds to wait for input

TTS_ENGINE = "pyttsx3" 
TTS_SPEED = 150 
TTS_VOICE = 1 

DEFAULT_BROWSER = "chrome"  

# OpenAI API configuration
OPENAI_API_KEY = "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"  # Replace with your OpenAI API key
openai.api_key = OPENAI_API_KEY

APP_PATHS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\system32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe"
}

DEBUG = True

NLP_MODE = "keywords"  # Options: "keywords", "openai"

COMMANDS = {
    "open_google": ["open google", "search google"],
    "open_youtube": ["open youtube", "play video"],
    "open_notepad": ["open notepad", "start notepad"],
    "exit": ["exit", "goodbye"]
}
