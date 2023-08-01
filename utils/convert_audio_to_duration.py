def convert_audio_to_duration(file_path: str):
    from pydub import AudioSegment
    try:
        audio = AudioSegment.from_file(file_path)
        duration_ms = len(audio)
        duration_sec = duration_ms / 1000.0

        hours = int(duration_sec / 3600)
        minutes = int((duration_sec % 3600) / 60)
        seconds = int(duration_sec % 60)
        return int(duration_sec), hours, minutes, seconds
    except Exception as e:
        print("Error:", str(e))
        return None

def second_to_hms(seconds: int):
    import datetime
    return "{:0>8}".format(str(datetime.timedelta(seconds=seconds)))

def hms_to_second(hms: str):
    if hms.count(":") < 2:
        raise ValueError("Not correct format")
    def to_int(n):
        return int(n)
    [hour, minute, second] = list(map(to_int,hms.split(":")))
    return hour * 3600 + minute * 60 + second
