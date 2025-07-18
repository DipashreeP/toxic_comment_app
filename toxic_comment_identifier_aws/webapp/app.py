import streamlit as st
from mcp import process_comment

st.set_page_config(
    page_title="Toxic Comment Rewriter",
    page_icon="🛡️",
    layout="centered",
)

st.title("Toxic Comment Rewriter")

user_input = st.text_area("Enter a comment to rewrite:")

if st.button("Rewrite"):
    if user_input.strip():
        rewritten = process_comment(user_input)
        st.success("Rewritten Comment:")
        st.write(rewritten)
    else:
        st.warning("Please enter a comment.") 