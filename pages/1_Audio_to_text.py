import logging
import os
import streamlit as st
import whisper
from component.page_meta import page_meta
from processing.audio_to_text_process import audio_to_text
from constants.temporary import TMP_DIR
from utils.pre_processing import pre_processing

page_meta(page_title="Audio to text", page_icon="🔤")

if "abort_loading" not in st.session_state:
    st.session_state.abort_loading = False

st.subheader("Load model")
model_type = st.selectbox(
    'Choose model type',
    ('tiny', 'base')) # ,'small', 'medium', 'large'
btn = st.button("Load")
if model_type in ["small","medium","large"]:
    st.warning("The better the model, the longer the load time")

if btn:
    st.session_state.abort_loading = False
    with st.spinner("Loading..."):
        if not st.session_state.abort_loading:
            if st.button("Cancel"):
                st.session_state.abort_loading = True
                st.experimental_rerun()

            w = whisper.load_model(model_type)
            st.success(f"Loaded {str(model_type).upper()} model")


st.subheader("Generate")
option = st.selectbox(
    'Choose file type (txt, srt)',
    ('txt', 'srt'))

file = st.file_uploader(label="Upload your audio file", accept_multiple_files=False, type=["mp3", "wav"])
if file is not None:
    btn = st.button("Generate", use_container_width=True, type="primary")
    if btn:
        file_name = file.name
        AUDIO_FILE = os.path.join(TMP_DIR, file_name)
        pre_processing(AUDIO_FILE)
        with open(AUDIO_FILE, "wb+") as f:
            f.write(file.read())
            f.close()
        file.close()
        file_type = option
        success = False
        with st.spinner("Loading"):
            result, transcribe, transcribe_arr = audio_to_text(audio_file=AUDIO_FILE, file_type=file_type, model_type=model_type)
            success = True
        if success:
            st.success("Completed!")
            st.subheader("Original audio")
            st.audio(AUDIO_FILE)
            st.subheader("Preview")
            with st.expander("Expand"):
                st.code(transcribe, language="plaintext")
            FILENAME_NO_EXT = file_name.split(".")[0]
            TRANS_FILENAME = f"{FILENAME_NO_EXT}.{file_type}"
            TRANS_FILE = os.path.join(TMP_DIR, TRANS_FILENAME)
            pre_processing(TRANS_FILE)
            with open(TRANS_FILE, "wb+") as f:
                f.write(bytes(transcribe, encoding='utf-8'))
                f.close()
            with open(TRANS_FILE, "rb") as f:
                btn = st.download_button(label="Download", data=f, file_name=TRANS_FILENAME, use_container_width=True)
                f.close()
            logging.info("AUDIO_TO_TEXT")
            print("AUDIO_TO_TEXT")
            try:
                os.remove(AUDIO_FILE)
                os.remove(TRANS_FILE)
            except OSError:
                print("Can't remove")
                pass
