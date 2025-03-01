import json
import os

with open(os.path.join(os.path.dirname(__file__), "intents.json")) as file:
    intents = json.load(file)

def process_command(command):
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in command:
                return intent, command.replace(pattern, "").strip()
    return "unknown", command
