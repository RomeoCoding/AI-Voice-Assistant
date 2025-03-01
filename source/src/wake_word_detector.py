import pvporcupine
from pvrecorder import PvRecorder
import config

def wake_word_listener(callback):
    try:
        # Initialize Porcupine with the desired wake word
        porcupine = pvporcupine.create(
            access_key="EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g==",
            keywords=[config.WAKE_WORD]  # Use the wake word from config
        )

        # Set up the recorder with the correct frame length
        recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

        # Start recording
        recorder.start()

        print("Listening for wake word...")

        while True:
            # Read and process the audio
            keyword_index = porcupine.process(recorder.read())

            # If a keyword is detected, invoke the callback
            if keyword_index >= 0:
                print(f"Wake word '{config.WAKE_WORD}' detected!")
                callback()  # Trigger the callback to handle wake word detection
                break  # Exit loop after detection

    except Exception as e:
        print(f"Error in wake word detection: {e}")
    finally:
        # Clean up
        recorder.stop()
        porcupine.delete()
        recorder.delete()
