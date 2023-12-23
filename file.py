from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave
import queue
import sys
import sounddevice as sd

SetLogLevel(0)

wf = wave.open("model/test/test.wav", "rb")
model = Model("model/")
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())