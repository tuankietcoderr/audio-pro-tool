COMPRESS_SAMPLE_RATE = 44100
COMPRESS_CHANNEL = 2
COMPRESS_FORMAT = "wav"
COMPRESS_DEFAULT_BITRATE = '64K'
COMMON_SAMPLE_RATES_LIST = ["8k", "16K", "44.1K", "48K","96K","192K","384K"]
COMMON_SAMPLE_RATES_LIST_INT = [8000, 16000,44100,48000,96000,192000,384000]
def get_audio_info(audio):
    channels = audio.channels
    frame_rate = audio.frame_rate
    bits_per_sample = audio.sample_width * 8
    bitrate = frame_rate * channels * bits_per_sample
    return frame_rate,channels,bitrate
