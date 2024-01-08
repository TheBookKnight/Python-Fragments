import speech_recognition as sr
from pydub import AudioSegment
import os

# Enter the file you want to transcribe
filename = input("Enter the mp4 file name: ")

# Load the video file
video = AudioSegment.from_file(filename)
# set audio to 16kHz at 16-bit
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export("audio.wav", format="wav")

# initialize the recognizer class (for recognizing the speech)
r = sr.Recognizer()

# open the audio file
with sr.AudioFile("audio.wav") as source:
    audio_text = r.record(source)
# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='en-US')

# Print the transcript
file_name = "transcription.txt"

with open(file_name, "w") as file:
    # Write to the file
    file.write(text)

# Open the file for editing by the user
os.system(f"start {file_name}")
