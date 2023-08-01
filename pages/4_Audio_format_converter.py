from component.page_meta import page_meta
import streamlit as st
import os
import logging
from utils.pre_processing import pre_processing
from constants.temporary import TMP_DIR
from pydub import AudioSegment

page_meta(page_title="Audio format converter", page_icon="🔄", is_under_construction=False)

support_ext_list = ["mp3", "wav", "oga"]
support_upload_list = ["mp3", "wav", "oga","flv", "ogg", "mogg", "mpc", "m4a", "flac", "aiff", "aa", "aac", "aax", "au", "m4p", "msv", "wma", "webm"]

file = st.file_uploader(label="Upload your audio file", accept_multiple_files=False, type=support_upload_list)

if file is not None:
    file_name = file.name
    current_file_ext = file_name.split(".")[-1]
    AUDIO_FILE = os.path.join(TMP_DIR, file_name)
    pre_processing(AUDIO_FILE)
    with open(AUDIO_FILE, "wb+") as f:
        f.write(file.read())
        f.close()
    file.close()
    audio = AudioSegment.from_file(AUDIO_FILE)
    st.markdown(f"Current audio extension: `{current_file_ext}`")
    st.write("Choose new audio extension")
    temp_ext_list = support_ext_list
    temp_ext_list.remove(current_file_ext)
    new_ext = st.selectbox("Current support extensions", temp_ext_list)
    SAVED_AUDIO = AUDIO_FILE.replace(current_file_ext, new_ext)
    if st.button("Convert"):
        with st.spinner("Loading..."):
            audio.export(SAVED_AUDIO, format=new_ext)
            st.audio(SAVED_AUDIO, format=f"audio/{new_ext.replace('mp3','mpeg').replace('oga','ogg')}")
        logging.info("AUDIO_FORMAT_CONVERTER")
        print("AUDIO_FORMAT_CONVERTER")
    try:
        os.remove(AUDIO_FILE)
        os.remove(SAVED_AUDIO)
    except OSError:
        pass
