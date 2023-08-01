import logging
from component.page_meta import page_meta
import streamlit as st
from utils.convert_audio_to_duration import convert_audio_to_duration,second_to_hms,hms_to_second
from constants.temporary import TMP_DIR
import os
from utils.pre_processing import pre_processing

page_meta(page_title="Audio cutter", page_icon="✂")

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
    total_second, hour, minute, second = convert_audio_to_duration(AUDIO_FILE)
    col1, col2 = st.columns(2)
    with col1:
        start = st.text_input("Start", placeholder=second_to_hms(0), value=second_to_hms(0))
        start_to_sec = 0
        if start:
            start_to_sec = hms_to_second(start)
            if start_to_sec > total_second:
                raise ValueError("Start time can't be greater than total time")
    with col2:
        end = st.text_input("End", placeholder=second_to_hms(total_second), value=second_to_hms(total_second))
        end_to_sec = total_second
        if end:
            end_to_sec = hms_to_second(end)
            if end_to_sec > total_second:
                raise ValueError("End time can't be greater than total time")
    start_time_ms = start_to_sec * 1000
    end_time_ms = end_to_sec * 1000
    btn = st.button("Export",use_container_width=True)
    if btn:
        with st.spinner("Loading"):
            from pydub import AudioSegment
            audio = AudioSegment.from_file(AUDIO_FILE)
            res = audio[start_time_ms:end_time_ms]
            SAVED_FILE = AUDIO_FILE.replace(file_ext, "wav")
            res.export(SAVED_FILE, format="wav")
            st.audio(SAVED_FILE)
            logging.info("AUDIO_CUTTER")
            print("AUDIO_CUTTER")
            try:
                os.remove(SAVED_FILE)
                os.remove(AUDIO_FILE)
            except OSError:
                pass

