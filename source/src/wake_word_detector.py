import pvporcupine
import pyaudio
import sys
sys.path.append("C:/Users/matro/AI-Voice-Assistant/source")  # Add the path to your config.py directory
import config
import os
def wake_word_listener(callback):
    try:
        # Set the correct wake word from config, like "picovoice" or any valid one
        access_key = "EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g=="
        porcupine = pvporcupine.create(
            keyword_paths=[pvporcupine.KEYWORD_PATHS[config.WAKE_WORD]],
            access_key=access_key  # Pass the access key here
        )
        # Start audio stream
        pa = pyaudio.PyAudio()
        stream = pa.open(rate=porcupine.sample_rate,
                         channels=1,
                         format=pyaudio.paInt16,
                         input=True,
                         frames_per_buffer=porcupine.frame_length)

        print("Listening for wake word...")

        while True:
            pcm = stream.read(porcupine.frame_length)
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                callback()  # Call the assistant after detecting the wake word
                break  # Exit the loop to start the assistant

    except Exception as e:
        print(f"Error in wake word detection: {e}")
