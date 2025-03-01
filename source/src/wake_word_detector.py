import pvporcupine
import pyaudio

def wake_word_listener(callback):
    try:
        # Set the access key (Make sure to replace this with your actual key)
        access_key = "EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g=="
        
        # Create the Porcupine instance using built-in keywords
        porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=["porcupine", "bumblebee"]  # Use the built-in keywords
        )

        # Start the audio stream with the correct frame length
        pa = pyaudio.PyAudio()
        
        # Convert the frame length to an integer
        frame_length = int(porcupine.frame_length / 2)  # Ensure it's an integer

        stream = pa.open(rate=porcupine.sample_rate,
                         channels=1,
                         format=pyaudio.paInt16,
                         input=True,
                         frames_per_buffer=frame_length)

        print("Listening for wake word...")

        while True:
            # Read the next audio frame
            pcm = stream.read(frame_length)  # Ensure it's an integer

            # Process the audio frame with Porcupine
            keyword_index = porcupine.process(pcm)

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
