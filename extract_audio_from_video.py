# import os
from moviepy.editor import VideoFileClip
# import speech_recognition as sr
# from pydub import AudioSegment
import simple_image_generator

def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

# def transcribe_audio(audio_path, language="en-US"):
#     recognizer = sr.Recognizer()
#     audio_file = sr.AudioFile(audio_path)
    
#     with audio_file as source:
#         audio_data = recognizer.record(source)
    
#     try:
#         text = recognizer.recognize_google(audio_data, language=language)
#         return text
#     except sr.UnknownValueError:
#         return ""
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         return ""

# def generate_captions(video_path, audio_path, language="en-US"):
#     # Extract audio from video
#     extract_audio_from_video(video_path, audio_path)
    
#     # Transcribe audio
#     text = transcribe_audio(audio_path, language)
    
#     return text

# Paths
video_path = f"{simple_image_generator.desktop_path}/Notification_Type_Issues.mov"
audio_path = "temp_audio.wav" 

extract_audio_from_video(video_path, audio_path)

# Generate captions
# captions_text = generate_captions(video_path, audio_path, language="en-US")  # Use "ar-SA" for Arabic

# # Print captions
# print("Captions:")
# print(captions_text)

# # Save captions to a file
# with open("captions.txt", "w", encoding="utf-8") as f:
#     f.write(captions_text)

# # Clean up temporary audio file
# os.remove(audio_path)


