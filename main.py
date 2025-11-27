import streamlit as st
from data.few_shot import FewShotPosts
from data.post_generator import generate_post
import os
print("CURRENT WORKING DIRECTORY:", os.getcwd())

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Generator")

    fs = FewShotPosts("data/processed_posts.json")
    tags = fs.get_tags()

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate Post"):
        post = generate_post(
            length=selected_length,
            language=selected_language,
            tag=selected_tag
        )
        st.subheader("Generated LinkedIn Post:")
        st.write(post)

if __name__ == "__main__":
    main()
