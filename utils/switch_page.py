
def switch_page(page: str, title: str):
    import streamlit as st
    return f'<a href="{page}" target="_self">{title}</a>'