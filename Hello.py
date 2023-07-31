import streamlit as st
from component.page_meta import page_meta

page_meta(page_title="Welcome", page_icon="👋",show_title=False)

st.markdown(
    """
    # Welcome to Audio Pro Tool 👋
    ## Your All-in-One Audio Tool Website!

    Audio Pro Tool is your ultimate destination for seamless audio management, offering a suite of powerful tools to 
    enhance your audio projects. Whether you're a content creator, podcaster, musician, or professional, 
    our feature-rich platform caters to all your audio needs.

    Key Features:

    1. **Audio to Text/Subtitle Converter**: Transform your audio files into accurate text or subtitle transcriptions 
    effortlessly. Our advanced speech recognition technology ensures precise conversion, saving you time and effort 
    in manual transcription.

    2. **Background Noise Reduction**: Say goodbye to distracting background noise with our cutting-edge noise 
    reduction feature. Remove unwanted hums, hisses, and ambient sounds, leaving your audio crisp and clear.

    3. **Audio Cutter and Editor**: Our intuitive audio cutter allows you to trim, crop, and merge audio files with 
    utmost precision. Seamlessly cut out specific segments, create loops, or craft seamless transitions for a 
    flawless audio experience.

    4. **Audio Format Converter**: Supports a wide range of audio formats, including MP3, WAV, FLAC, AAC, OGG, WMA, 
    and more. Whatever your input format may be, our converter effortlessly transforms your audio files to the 
    desired output format.

    5. **Audio Compression**: Compress large audio files without compromising on quality using our efficient audio 
    compression tool. Reduce file sizes for easy sharing and storage, while maintaining the integrity of your sound.

    6. **Audio Processing Made Easy**: Unleash the full potential of your audio recordings with our sophisticated 
    audio processing tools. Enhance clarity, adjust volumes, balance frequencies, and apply dynamic effects to 
    achieve a professional-grade sound.

    7. **Real-Time Preview**: Experience the changes in real-time with our instant preview feature. Fine-tune your 
    audio settings and observe the impact on the waveform as you make adjustments.
    
    Experience the power of Audio Pro Tool and revolutionize your audio creations. Unlock endless possibilities with 
    our comprehensive set of tools designed to elevate your projects to new heights. Sign up now and embark on a 
    remarkable audio journey with Audio Pro Tool!"""
)