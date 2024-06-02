
import speech_recognition as sr
from faster_whisper import WhisperModel
import ffmpeg
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


video_path = f"{desktop_path}/Notification_Type_Issues.mov"
input_video = video_path
input_video_name = input_video.replace(".mov", "")


def extract_audio():
    extracted_audio = f"{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

def transcribe(audio):
    model = WhisperModel("small")
    segments, info = model.transcribe(audio)
    language = info[0]
    print("Transcription language", info[0])
    segments = list(segments)
    
    for segment in segments:
    # Convert seconds to hours, minutes, and seconds
     start_hours, start_minutes = divmod(segment.start, 3600)
     start_minutes, start_seconds = divmod(start_minutes, 60)
     start_milliseconds = int((segment.start - int(segment.start)) * 1000)
    
     end_hours, end_minutes = divmod(segment.end, 3600)
     end_minutes, end_seconds = divmod(end_minutes, 60)
     end_milliseconds = int((segment.end - int(segment.end)) * 1000)
    
    # Format the time values
     start_timecode = "%02d:%02d:%02d,%03d" % (start_hours, start_minutes, start_seconds, start_milliseconds)
     end_timecode = "%02d:%02d:%02d,%03d" % (end_hours, end_minutes, end_seconds, end_milliseconds)
     print(segments.index(segment) + 1)
     print("%s --> %s\n%s"%(start_timecode, end_timecode, segment.text))
     print("")
        # print(segment)
        # print("[%.2fs --> %.2fs] %s" %
        #         (segment.start, segment.end, segment.text))
    return language, segments


extracted_audio = extract_audio()
language, segments = transcribe(audio=extracted_audio)