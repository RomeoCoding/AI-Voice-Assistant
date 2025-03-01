import openai
from config import open_ai_key, NLP_MODE, COMMANDS

# Function to handle processing commands
def process_command(command):
    if NLP_MODE == "keywords":
        return process_keywords(command)
    elif NLP_MODE == "openai":
        return process_gpt(command)
    else:
        return "unknown", []

# Function for keyword-based command processing
def process_keywords(command):
    for intent, synonyms in COMMANDS.items():
        for synonym in synonyms:
            if synonym in command.lower():
                return intent, []
    return "unknown", []

# Function for GPT-based command processing
def process_gpt(command):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change this to another model if necessary
            prompt=command,
            max_tokens=150,  # Adjust as needed
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return "gpt_response", answer
    except Exception as e:
        return "error", str(e)
