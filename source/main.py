from src.wake_word_detector import wake_word_listener
from src.my_speech_recognition import recognize_speech
from src.nlp_processor import process_command
from src.command_executor import execute_command
from src.tts import speak

def start_assistant():
    speak("Hello! I am your AI Assistant. How can I help you?")

    while True:
        # Wait for the user to speak a command
        command = recognize_speech()

        # If the assistant couldn't hear anything, retry
        if command:
            print(f"Received command: {command}")
            intent, params = process_command(command)
            
            if intent == "exit":
                speak("Goodbye!")
                break  # Exit the assistant
            
            if intent == "gpt_response":
                speak(params)  # Speak the response from GPT
            else:
                execute_command(intent, params)  # Execute predefined commands
        else:
            speak("Sorry, I didn't catch that. Try again.")

if __name__ == "__main__":
    # Start the assistant only after detecting the wake word
    print("Assistant is listening for the wake word...")
    wake_word_listener(start_assistant)  # Calls start_assistant() after detecting "hey assistant"
