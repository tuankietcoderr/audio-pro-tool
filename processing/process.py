from datetime import timedelta
import srt
import whisper
from os.path import join as join_path
from typing import List, Optional, Sequence, Union, cast, overload
from numpy import ndarray
import ffmpeg
import numpy as np

def transcribe_time_stamps(segments: list):
    string = ""
    for seg in segments:
        string += "".join([str(seg["start"]), "->", str(seg["end"]), ": ", seg["text"].strip(), "\n"])
    return string


def transcribe_time_stamps_arr(segment: list):
    arr = []
    for seg in segment:
        arr.append({
            "start_at": float(seg["start"]),
            "end_at": float(seg["end"]),
            "text": seg["text"].strip()
        })
    return arr


def make_srt_subtitles(segments: list):
    subtitles = []
    for i, seg in enumerate(segments, start=1):
        start_time = seg["start"]
        end_time = seg["end"]
        text = seg["text"].strip()

        subtitle = srt.Subtitle(
            index=i,
            start=timedelta(seconds=start_time),
            end=timedelta(seconds=end_time),
            content=text
        )
        subtitles.append(subtitle)

    return srt.compose(subtitles)


def speech_processing(audio_file: str, model_type: Optional[str] = "tiny", file_type:  Optional[str] = "srt", file_name: Optional[str] = "subtitle", timestamps: bool = True):
    model = whisper.load_model(model_type.lower())
    result = model.transcribe(audio=whisper.load_audio(audio_file), fp16=False)

    # Create the subtitle file
    # subtitle_file = join_path(PROJECT_DIR_TO_DOWNLOAD_FILE, f"{file_name}.{file_type}")
    transcribe = ""
    transcribe_arr = transcribe_time_stamps_arr(result["segments"])
    if file_type == "srt":
        # with open(subtitle_file, "w", encoding='utf-8') as f:
        if timestamps:
            tmp = make_srt_subtitles(result["segments"])
            transcribe = tmp
            # f.write(tmp)
            # f.close()
        else:
            transcribe = result["text"]
            # f.write(result["text"])
            # f.close()
    elif file_type == "txt":
        # with open(subtitle_file, "w", encoding='utf-8') as f:
        transcribe = result["text"]
        # f.write(result["text"])
        # f.close()

    else:
        raise TypeError("Invalid file type")
    return result, transcribe, transcribe_arr