from transformers import pipeline
speech_recognizer = pipeline("automatic-speech-recognition")
audio_file = "C:\Users\Ahmed Khaled\Desktop\hello-48300.mp3"
transcription = speech_recognizer(audio_file)["text"]
