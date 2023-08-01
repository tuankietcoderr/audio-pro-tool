from df.enhance import enhance, init_df, load_audio, save_audio
import streamlit as st
import os
from component.page_meta import page_meta
from pydub import AudioSegment
from constants.temporary import TMP_DIR
from utils.pre_processing import pre_processing

UNDER_CONSTRUCTION = False
page_meta(page_title="Background noise reduction", page_icon="🎸", is_under_construction=UNDER_CONSTRUCTION)
if not UNDER_CONSTRUCTION:
    file = st.file_uploader(label="Upload your audio file", accept_multiple_files=False, type=["mp3", "wav"])
    if file is not None:
        btn = st.button("Enhance")
        if btn:
            file_name = file.name
            file_ext = file_name.split(".")[-1]
            AUDIO_FILE = os.path.join(TMP_DIR, file_name)
            pre_processing(AUDIO_FILE)
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
                try:
                    os.remove(AUDIO_FILE)
                except OSError:
                    pass
                AUDIO_FILE = dst
            os.system("df -h")
            with st.spinner("Loading"):
                try:
                    model, df_state, _ = init_df()
                    # Download and open some audio file. You use your audio files here
                    audio, _ = load_audio(AUDIO_FILE, sr=df_state.sr())
                    # Denoise the audio
                    enhanced = enhance(model, df_state, audio)
                    # Save for listening
                    ENHANCE_AUDIO = f"enhanced_{file_name}"
                    SAVED_AUDIO = os.path.join(TMP_DIR, ENHANCE_AUDIO)
                    pre_processing(SAVED_AUDIO)
                    save_audio(SAVED_AUDIO, enhanced, df_state.sr())
                    st.success("Completed!")
                    st.markdown("### Before")
                    st.audio(AUDIO_FILE)
                    st.markdown("### After")
                    st.audio(SAVED_AUDIO)
                except OSError:
                    st.error("Error while processing audio. Please try again!")
                    pass
            try:
                os.remove(SAVED_AUDIO)
            except OSError:
                print("Can't remove")
                pass
