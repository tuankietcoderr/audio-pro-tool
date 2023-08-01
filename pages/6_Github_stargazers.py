from component.page_meta import page_meta
import requests
import streamlit as st

page_meta(page_title="Github stargazers", page_icon="https://cdn-icons-png.flaticon.com/512/25/25231.png")


def get_stargazers_data():
    try:
        response = requests.get("https://api.github.com/repos/tuankietcoderr/audio-pro-tool/stargazers",
                                json={'key': 'value'})
        if response.status_code == 200:
            return response.json()
        return None
    except ConnectionError:
        return None


data = get_stargazers_data()
if data is not None:
    for user in data:
        col1, col2 = st.columns([1,9])
        with col1:
            st.image(user["avatar_url"])
        with col2:
            st.markdown(f"[**{user['login']}**]({user['html_url']})")

else:
    st.info("No users star this project")
