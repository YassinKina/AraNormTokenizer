import streamlit as st
from normalize import normalize_arabic
from tokenize_text import tokenize_arabic

st.set_page_config(page_title="Arabic Text Normalization & Tokenization Tool")
st.title("📚 Arabic Text Normalizer & Tokenizer")

st.markdown("""
This tool allows you to normalize and tokenize Arabic text for NLP preprocessing.
""")

text_input = st.text_area("Enter Arabic Text:", height=150)

apply_normalization = st.checkbox("Apply Normalization", value=True)
apply_tokenization = st.checkbox("Apply Tokenization", value=True)

if st.button("Process"):
    if not text_input.strip():
        st.warning("Please enter some Arabic text.")
    else:
        normalized_text = normalize_arabic(text_input) if apply_normalization else text_input
        tokens = tokenize_arabic(normalized_text) if apply_tokenization else [normalized_text]

        st.subheader("Results")
        st.markdown("**Normalized Text:**")
        st.code(normalized_text, language="text")

        if apply_tokenization:
            st.markdown("**Tokens:**")
            st.code(tokens, language="python")
