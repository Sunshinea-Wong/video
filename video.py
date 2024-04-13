import streamlit as st

upload_file=st.file_uploader('video',type=['mp4'])
if upload_file is not None:
    st.video(upload_file)


