import streamlit as st
from app.services.post_service import PostService

service = PostService()

def run_ui():

    st.set_page_config(page_title="AI LinkedIn Generator", layout="wide")

    st.markdown("""
    <style>
    .block-container {padding-top: 2rem;}
    button {height: 3em; font-size: 16px;}
    </style>
    """, unsafe_allow_html=True)

    st.title("🚀 AI LinkedIn Post Generator")
    st.caption("Generate high-quality posts in your style")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        tag = st.selectbox("Topic", service.get_tags())

    with col2:
        length = st.selectbox("Length", ["Short","Medium","Long"])

    with col3:
        language = st.selectbox("Language", ["English","Hinglish"])

    with col4:
        tone = st.selectbox(
            "Tone",
            ["Professional","Storytelling","Motivational","Personal"]
        )

    hooks = st.checkbox("Generate multiple hook options")

    if st.button("✨ Generate Post", use_container_width=True):

        with st.spinner("Generating..."):
            post = service.generate(tag, length, language, tone, hooks)

        st.markdown("### 📝 Generated Post")
        st.code(post, language="markdown")
