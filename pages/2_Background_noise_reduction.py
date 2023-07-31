from df.enhance import enhance, init_df, load_audio, save_audio
import streamlit as st
import os
from component.page_meta import page_meta
from pydub import AudioSegment

page_meta(page_title="Background noise reduction", page_icon="🎸")
TMP_DIR = os.path.join(os.getcwd(), "tmp")

file = st.file_uploader(label="Upload your audio file", accept_multiple_files=False, type=["mp3", "wav"])
if file is not None:
    btn = st.button("Enhance")
    if btn:
        file_name = file.name
        file_ext = file_name.split(".")[-1]
        AUDIO_FILE = os.path.join(TMP_DIR, file_name)
        with open(AUDIO_FILE, "wb+") as f:
            f.write(file.read())
            f.close()
        file.close()
        if file_ext == "mp3":
            src = AUDIO_FILE
            dst = AUDIO_FILE.replace("mp3", "wav")
            to_wav = AudioSegment.from_mp3(src)
            to_wav.export(dst, format="wav")
            file_name = file_name.replace("mp3", "wav")
            AUDIO_FILE = dst
        with st.spinner("Loading"):
            model, df_state, _ = init_df()
            # Download and open some audio file. You use your audio files here
            audio, _ = load_audio(AUDIO_FILE, sr=df_state.sr())
            # Denoise the audio
            enhanced = enhance(model, df_state, audio)
            # Save for listening
            ENHANCE_AUDIO = f"enhanced_{file_name}"
            SAVED_AUDIO = os.path.join(TMP_DIR, ENHANCE_AUDIO)
            save_audio(SAVED_AUDIO, enhanced, df_state.sr())
            st.success("Completed!")
            st.markdown("### Before")
            st.audio(AUDIO_FILE)
            st.markdown("### After")
            st.audio(SAVED_AUDIO)
        try:
            os.remove(AUDIO_FILE)
            os.remove(SAVED_AUDIO)
        except OSError:
            print("Can't remove")
            pass