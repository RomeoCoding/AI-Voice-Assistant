import openai
import os
import sys

# Add the parent directory (source) to sys.path so we can import config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from config
from config import openai_api_key, NLP_MODE, COMMANDS

# Initialize the OpenAI API with the key
openai.api_key = openai_api_key  # Make sure openai_api_key is properly set in your config.py or environment

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
    # Check if the command looks like a question (heuristic: contains a "?")
    if '?' in command:
        print("Processing command with GPT...")
        return "gpt_response", command  # Return the command to be processed by GPT

    # If not a question, check for predefined commands
    for intent, synonyms in COMMANDS.items():
        for synonym in synonyms:
            if synonym.lower() in command.lower():  
                print(f"Matched intent: {intent} with synonym: {synonym}")  # Debugging print
                return intent, []
    
    return "unknown", []

# Function for GPT-based command processing
def process_gpt(command):
    try:
        # Make an API call to OpenAI to process the user's question
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use other models as needed
            prompt=command,
            max_tokens=150,  # Adjust as needed
            temperature=0.7  # Adjust to control creativity (0.0 to 1.0)
        )
        # Extract the answer from GPT's response
        answer = response.choices[0].text.strip()
        print(f"GPT response: {answer}")  # Debugging print
        return "gpt_response", answer  # Return the response for speaking
    except Exception as e:
        print(f"Error during GPT query: {e}")
        return "error", str(e)  # Return error message in case of failure
