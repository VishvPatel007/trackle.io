import speech_recognition as sr

tempfile = sr.AudioFile('OSR_us_000_0010_8k.wav')
r = sr.Recognizer()

with tempfile as tf:
	r.adjust_for_ambient_noise(tf, duration=0.5)
	audio = r.record(tf)
	out = r.recognize_google(audio)
	print(out)
