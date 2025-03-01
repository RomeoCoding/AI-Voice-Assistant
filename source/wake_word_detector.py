import pvporcupine
import pyaudio
import struct
import config

def wake_word_listener(callback):
    porcupine = pvporcupine.create(keyword_paths=[pvporcupine.KEYWORD_PATHS[config.WAKE_WORD]])
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=porcupine.sample_rate,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word...")

    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        if porcupine.process(pcm) >= 0:
            print("Wake word detected!")
            callback()  # Calls the main assistant function

    stream.close()
    pa.terminate()
    porcupine.delete()
