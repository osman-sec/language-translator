from deep_translator import GoogleTranslator
from gtts import gTTS
import streamlit as st
import io

st.set_page_config(page_title="Language Translator", page_icon="🌍")
st.title("🌐 Language Translator + TTS")

# Input
text = st.text_area("Enter text to translate:", height=150)
src = st.text_input("Source language (auto for autodetect)", "auto")
target = st.text_input("Target language (e.g., en, bn, fr)", "en")
action = st.radio("Action", ["Translate", "Translate + TTS"])

# Button
if st.button("Submit"):
    if text.strip():
        try:
            translated = GoogleTranslator(source=src, target=target).translate(text)
            st.subheader("Translated:")
            st.write(translated)
        except Exception as e:
            st.error(f"Translation error: {e}")

        if action == "Translate + TTS":
            try:
                tts = gTTS(translated, lang=target)
                buf = io.BytesIO()
                tts.write_to_fp(buf)
                buf.seek(0)
                st.audio(buf, format="audio/mp3")
            except Exception as e:
                st.error(f"TTS error: {e}")
