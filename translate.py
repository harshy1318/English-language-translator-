import streamlit as st
import requests

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="English → Hindi Translator",
    page_icon="🇮🇳",
    layout="centered"
)

st.title("🤖 English → Hindi AI Translator")
st.write("Translate **any English word or sentence** into Hindi")

# ---------------- TRANSLATION FUNCTION ----------------
def translate_en_hi(text):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": "en",
        "target": "hi",
        "format": "text"
    }

    response = requests.post(url, data=payload)
    result = response.json()
    return result["translatedText"]

# ---------------- UI ----------------
text = st.text_area("Enter English text:")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            hindi = translate_en_hi(text)
            st.subheader("🇮🇳 Hindi Meaning")
            st.success(hindi)
        except:
            st.error("Translation service unavailable. Try again later.")
