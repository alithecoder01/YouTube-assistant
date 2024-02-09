import streamlit as st
import Langchain_helper as lgc 
import textwrap

st.title("Youtube Assistance")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label = "What is your youtube url: ",
            max_chars=80
        )
        query = st.sidebar.text_area(
            label="Ask about the vide: ",
            max_chars=50,
            key="query"
        )

        submit_btn = st.form_submit_button(
            label="Submit"
        )

if query and youtube_url:
    db = lgc.create_vector_db_from_youTube_url(youtube_url)
    respons = lgc.get_respons_from_quary(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(respons,width= 80))