import streamlit as st
from googletrans import Translator

st.title("Language Translator")
st.write("Languages Supported:-")
st.write("English: en, Spanish: es, French: fr, German: de, Hindi: hi, Chinese: zh-CN")

input_language = st.text_input("Enter the source language code (e.g., en for English):")
output_language = st.text_input("Enter the destination language code (e.g., fr for French):")
text_to_translate = st.text_area("Enter the text to translate:")

if st.button("Translate"):
    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=input_language, dest=output_language).text
    st.write("Translated Text:")
    st.write(translated_text)