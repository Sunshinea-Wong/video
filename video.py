import streamlit as st

st.markdown("""
<style>
.navbar {
    overflow: hidden;
    background-color: #333;
}

.navbar a {
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.navbar a:hover {
    background-color: #ddd;
    color: black;
}
</style>
""",unsafe_allow_html=True)
st.markdown("""
<div class="navbar">
    <a href="#">首页</a>
    <a href="#">新闻</a>
    <a href="#">联系</a>
    <a href="#">关于</a>
</div>
""", unsafe_allow_html=True)
upload_file=st.file_uploader('video',type=['mp4'])
if upload_file is not None:
    st.video(upload_file)


