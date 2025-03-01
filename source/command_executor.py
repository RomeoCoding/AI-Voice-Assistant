import webbrowser
import os
import pyautogui

def execute_command(intent, params):
    if intent == "open_website":
        webbrowser.open(f"https://www.{params}.com")
    elif intent == "search_google":
        webbrowser.open(f"https://www.google.com/search?q={params}")
    elif intent == "open_app":
        os.system(f"start {params}")  # Windows: "start", Linux/Mac: "open"
    elif intent == "type_text":
        pyautogui.write(params)
    elif intent == "exit":
        exit()
    else:
        print(f"Unknown command: {params}")
