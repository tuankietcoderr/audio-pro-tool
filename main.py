import streamlit as st
import whisper
from processing.process import speech_processing
# Title
st.title("Audio to text")

# Header
with st.form("Model"):
    st.subheader("Load model")
    model_type = st.selectbox(
        'Choose model type',
        ('tiny', 'base', 'small', 'medium'))
    btn = st.form_submit_button("Load")
    if btn:
        with st.spinner("Loading..."):
            whisper.load_model(model_type)
        st.success(f"Loaded {str(model_type).upper()} model")

st.subheader("Generate")
option = st.selectbox(
    'Choose file type (txt, srt)',
    ('txt', 'srt'))
file = st.file_uploader(label="Upload your audio file",accept_multiple_files=False,type=["mp3","wav"])
if file is not None:
    btn = st.button("Generate", use_container_width=True, type="primary")
    if btn:
        file_ext = file.name.split('.')[1]
        file_name = "test." + file_ext
        with open(f"tmp/{file_name}", "wb") as f:
            f.write(file.read())
            f.close()
        file.close()
        file_type = option
        success = False
        with st.spinner("Loading"):
            result, transcribe, transcribe_arr = speech_processing(audio_file=f"tmp/{file_name}",file_type=file_type)
            success = True
        if success:
            st.success("Completed!")
            st.subheader("Preview")
            with st.expander("Expand"):
                st.code(transcribe,language="plaintext")
            with open(f"tmp/transcribe.{file_type}", "wb") as f:
                f.write(bytes(transcribe,encoding='utf-8'))
                f.close()
            with open(f"tmp/transcribe.{file_type}","rb") as f:
                btn = st.download_button(label="Download",data=f,file_name=f"transcribe.{file_type}",use_container_width=True)
                f.close()
