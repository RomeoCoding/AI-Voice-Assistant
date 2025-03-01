import pvporcupine
import pyaudio


def wake_word_listener(callback):
    try:
        # Get the access key from environment variable (or set it here if needed)
        access_key = "EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g=="
        # Set the correct wake word to "porcupine" or "bumblebee"
        porcupine = pvporcupine.create(
            access_key=access_key,  # Pass in your access key here
            keywords=["porcupine", "bumblebee"]  # List the built-in wake words you want to use
        )

        # Start audio stream
        pa = pyaudio.PyAudio()
        stream = pa.open(rate=porcupine.sample_rate,
                         channels=1,
                         format=pyaudio.paInt16,
                         input=True,
                         frames_per_buffer=porcupine.frame_length  # Use the frame_length provided by Porcupine
                        )

        print("Listening for wake word...")

        while True:
            pcm = stream.read(porcupine.frame_length)  # Use porcupine.frame_length
            keyword_index = porcupine.process(pcm)  # Process the audio frame

            if keyword_index >= 0:  # If a keyword is detected
                if keyword_index == 0:
                    print("Wake word 'porcupine' detected!")
                elif keyword_index == 1:
                    print("Wake word 'bumblebee' detected!")
                
                callback()  # Call the assistant after detecting the wake word
                break  # Exit the loop to start the assistant

    except Exception as e:
        print(f"Error in wake word detection: {e}")
    finally:
        porcupine.delete()  # Release Porcupine resources after use
