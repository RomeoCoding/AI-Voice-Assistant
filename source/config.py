# config.py
import openai
import os

WAKE_WORD = "porcupine"  # Or any other valid keyword from the predefined set

SPEECH_RECOGNIZER = "google"  
SPEECH_TIMEOUT = 5  # Max seconds to wait for input

TTS_ENGINE = "pyttsx3" 
TTS_SPEED = 150 
TTS_VOICE = 1 

DEFAULT_BROWSER = "chrome"  

# OpenAI API configuration
openai.api_key = os.getenv("OPENAI_API_KEY")
openai_api_key=openai.api_key
APP_PATHS = {
    "chrome": "C:\Program Files\Google\Chrome\Application\chrome.exe",
}

DEBUG = True

NLP_MODE = "keywords"  # Options: "keywords", "openai"

COMMANDS = {
    "open_google": ["open google", "search google"],
    "open_youtube": ["open youtube", "play video"],
    "open_notepad": ["open notepad", "start notepad"],
    "exit": ["exit", "goodbye"]
}
