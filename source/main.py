from src.wake_word_detector import wake_word_listener
from src.speech_recognition import recognize_speech
from src.nlp_processor import process_command
from src.command_executor import execute_command
from src.tts import speak

def start_assistant():
    speak("Hello! I am your AI Assistant. How can I help you?")
    
    while True:
        command = recognize_speech()
        if command:
            intent, params = process_command(command)
            if intent == "exit":
                speak("Goodbye!")
                break
            execute_command(intent, params)
        else:
            speak("Sorry, I didn't catch that. Try again.")

if __name__ == "__main__":
    wake_word_listener(start_assistant)  # Runs assistant only after wake word
