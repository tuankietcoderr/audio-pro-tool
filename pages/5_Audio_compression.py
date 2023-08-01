import datetime

from component.page_meta import page_meta
from pydub import AudioSegment
import streamlit as st
from utils.pre_processing import pre_processing
from constants.temporary import TMP_DIR
import os
import logging
from processing.audio_compression_process import get_audio_info,COMMON_SAMPLE_RATES_LIST_INT

page_meta(page_title="Audio compression", page_icon="⏬", is_under_construction=False)


file = st.file_uploader(label="Upload your audio file", accept_multiple_files=False, type=["mp3", "wav"])
if file is not None:
    file_name = file.name
    file_ext = file_name.split(".")[-1]
    AUDIO_FILE = os.path.join(TMP_DIR, file_name)
    pre_processing(AUDIO_FILE)
    with open(AUDIO_FILE, "wb+") as f:
        f.write(file.read())
        f.close()
    file.close()
    audio = AudioSegment.from_file(AUDIO_FILE)
    frame_rate, channels, bitrate = get_audio_info(audio)
    st.markdown(f"Current video size: `{(os.path.getsize(AUDIO_FILE) / (1024 * 1024)):.2f}MB`")
    col1, col2 = st.columns(2)
    with col1:
        br = st.selectbox("Choose audio quality", (32,64,96,128,192,256,320))
    with col2:
        channel = st.selectbox("Select channel", ("Mono", "Stereo"))
    if st.button("Compress"):
        compressed_audio = audio.set_frame_rate(frame_rate).set_channels(1 if channel == "Mono" else 2)
        with st.spinner("Loading..."):
            compressed_audio.export(AUDIO_FILE, format="mp3", bitrate=str(br)+"K")
            st.markdown(f"After compressing: `{(os.path.getsize(AUDIO_FILE) / (1024 * 1024)):.2f}MB`")
            st.audio(AUDIO_FILE)
        logging.info("AUDIO_COMPRESSION")
        print("AUDIO_COMPRESSION")
        try:
            os.remove(AUDIO_FILE)
        except OSError:
            pass
