import sounddevice
from scipy.io.wavfile import write

print("Recording started")
rec = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
sounddevice.wait()
write(file, 44100, rec)
print("Recording completed")

