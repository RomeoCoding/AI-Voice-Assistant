import pvporcupine
import pyaudio

def wake_word_listener(callback):
    try:
        # Set the access key (Make sure to replace this with your actual key)
        access_key = "EdLqrYoN0zYuUFMpKuq3oKxgABeqBLCQjOPxpUV9Iea/NHN1prlN9g=="
        
        # Create the Porcupine instance using only one keyword for simplicity
        porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=["porcupine"]  # Test with just one keyword
        )

        # Start the audio stream with the correct frame length
        pa = pyaudio.PyAudio()
        frame_length = int(porcupine.frame_length / 2)  # Ensure it's an integer

        print(f"Porcupine frame length: {porcupine.frame_length}")
        
        stream = pa.open(rate=porcupine.sample_rate,
                         channels=1,
                         format=pyaudio.paInt16,
                         input=True,
                         frames_per_buffer=frame_length)

        print("Listening for wake word...")

        while True:
            # Read the next audio frame
            pcm = stream.read(frame_length)

            # Log the PCM length (make sure the stream is providing audio)
            print(f"Received audio frame of length: {len(pcm)}")

            # Process the audio frame with Porcupine
            keyword_index = porcupine.process(pcm)

            # Log the result of porcupine.process()
            print(f"Porcupine result: {keyword_index}")

            if keyword_index >= 0:  # If a keyword is detected
                if keyword_index == 0:
                    print("Wake word 'porcupine' detected!")

                callback()  # Call the assistant after detecting the wake word
                break  # Exit the loop to start the assistant

    except Exception as e:
        print(f"Error in wake word detection: {e}")
    finally:
        porcupine.delete()  # Release Porcupine resources after use
