import streamlit as st
from component.page_meta import page_meta
from utils.switch_page import switch_page

page_meta(page_title="Welcome", page_icon="👋", show_title=False)

st.markdown(
    f"""
    # Welcome to Audio Pro Tool 👋
    ## Your All-in-One Audio Tool Website!

    Audio Pro Tool is your ultimate destination for seamless audio management, offering a suite of powerful tools to 
    enhance your audio projects. Whether you're a content creator, podcaster, musician, or professional, 
    our feature-rich platform caters to all your audio needs.

    Key Features:

    1. {switch_page(title="**Audio to Text/Subtitle Converter**", page="/Audio_to_text")}: Transform your audio files into accurate text or subtitle transcriptions 
    effortlessly. Our advanced speech recognition technology ensures precise conversion, saving you time and effort 
    in manual transcription.

    2. {switch_page(title="**Background Noise Reduction**", page="/Background_noise_reduction")}: Say goodbye to distracting background noise with our cutting-edge noise 
    reduction feature. Remove unwanted hums, hisses, and ambient sounds, leaving your audio crisp and clear.

    3. {switch_page(title="**Audio Cutter**", page="/Audio_cutter")}: Our intuitive audio cutter allows you to trim, audio files with 
    utmost precision.

    4. {switch_page(title="**Audio Format Converter**", page="/Audio_format_converter")}: Supports a wide range of audio formats, including MP3, WAV, FLAC, AAC, OGG, WMA, 
    and more. Whatever your input format may be, our converter effortlessly transforms your audio files to the 
    desired output format.

    5. {switch_page(title="**Audio Compression**", page="/Audio_compression")}: Compress large audio files without compromising on quality using our efficient audio 
    compression tool. Reduce file sizes for easy sharing and storage, while maintaining the integrity of your sound.
    
    Experience the power of Audio Pro Tool and revolutionize your audio creations. Unlock endless possibilities with 
    our comprehensive set of tools designed to elevate your projects to new heights. Sign up now and embark on a 
    remarkable audio journey with Audio Pro Tool!"""
    , unsafe_allow_html=True
)
