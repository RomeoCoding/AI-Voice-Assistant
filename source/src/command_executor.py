import webbrowser
import os
import pyautogui
def execute_command(intent, params):
    if intent == "open_website":
        if params:
            webbrowser.open(f"https://www.{params}.com")
        else:
            print("No website provided.")
    elif intent == "search_google":
        if params:
            webbrowser.open(f"https://www.google.com/search?q={params}")
        else:
            print("No search query provided.")
    elif intent == "open_app":
        if params:
            os.system(f"start {params}")  # Windows: "start", Linux/Mac: "open"
        else:
            print("No app name provided.")
    elif intent == "type_text":
        if params:
            pyautogui.write(params)
        else:
            print("No text provided to type.")
    elif intent == "exit":
        exit()
    else:
        print(f"Unknown command: {params}")
