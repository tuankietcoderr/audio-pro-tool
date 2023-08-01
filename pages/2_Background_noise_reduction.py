import streamlit as st
import os
import logging
from component.page_meta import page_meta
from pydub import AudioSegment
from constants.temporary import TMP_DIR
from utils.pre_processing import pre_processing
import noisereduce as nr
import numpy as np

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
            with st.spinner("Loading"):
                audio = AudioSegment.from_file(AUDIO_FILE)
                # Convert Pydub AudioSegment object to NumPy array
                samples = audio.get_array_of_samples()
                sample_rate = audio.frame_rate
                reduced_noise = nr.reduce_noise(y=samples, sr=sample_rate)
                reduced_audio = audio._spawn(reduced_noise.astype(np.int16))
                ENHANCE_AUDIO = f"enhance_{file_name}"
                SAVED_AUDIO = os.path.join(TMP_DIR, ENHANCE_AUDIO)
                reduced_audio.export(SAVED_AUDIO, format="wav")
            st.success("Completed!")
            st.markdown("### Before")
            st.audio(AUDIO_FILE)
            st.markdown("### After")
            st.audio(SAVED_AUDIO)
            logging.info("BACKGROUND_NOISE_REDUCTION")
            print("BACKGROUND_NOISE_REDUCTION")
            try:
                os.remove(SAVED_AUDIO)
                os.remove(AUDIO_FILE)
            except OSError:
                print("Can't remove")
                pass
