import pvporcupine
import pyaudio
import config

def wake_word_listener(callback):
    try:
        # Set the correct wake word from config, like "picovoice" or any valid one
        porcupine = pvporcupine.create(keyword_paths=[pvporcupine.KEYWORD_PATHS[config.WAKE_WORD]])

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
