import pvporcupine
import pyaudio
import sys
sys.path.append("C:/Users/matro/AI-Voice-Assistant/source")  # Add the path to your config.py directory
import config

def wake_word_listener(callback):
    try:
        # Make sure config.WAKE_WORD has a valid wake word like 'porcupine'
        access_key = "EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g=="
        
        # Use the correct wake word from config
        porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=[config.WAKE_WORD]  # Ensure this matches a valid keyword like "porcupine" or "bumblebee"
        )

        # Start audio stream
        pa = pyaudio.PyAudio()
        frame_length = int(porcupine.frame_length / 2)
        stream = pa.open(rate=porcupine.sample_rate,
                         channels=1,
                         format=pyaudio.paInt16,
                         input=True,
                         frames_per_buffer=frame_length)

        print("Listening for wake word...")

        while True:
            pcm = stream.read(frame_length*2)
            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:  # Check if any keyword was detected
                print("Wake word detected!")
                callback()  # Call the assistant after detecting the wake word
                break  # Exit the loop to start the assistant

    except Exception as e:
        print(f"Error in wake word detection: {e}")
    finally:
        porcupine.delete()  # Explicitly release resources after use
