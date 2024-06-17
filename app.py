# Importing libraries
import streamlit as st
import speech_recognition as sr
import openai
import time
import os

# Setting Webpage Configurations
st.set_page_config(page_icon="🎤", page_title="Airbnb", layout="wide")

st.title(":rainbow: Speech to Text with ChatGPT :loud_sound:")

st.divider()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
record = st.button(':violet_circle: Voice Search 🔍')

if record:
    with sr.Microphone() as source:
        st.caption("Say something...")
        audio = recognizer.listen(source, phrase_time_limit=5)  # Increase time limit if necessary

    # Recognize the audio
    try:
        text = recognizer.recognize_google(audio)  # You can choose a different recognition engine/API
        st.caption(f"Prompt : {text}")

        # Initialize OpenAI with API key
        openai.api_key = os.getenv('OPENAI_API_KEY')  # Load API key from environment variable

        prompt_text = text

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            max_tokens=3500
        )

        with st.spinner('Loading....'):
            time.sleep(2)
        st.code(response['choices'][0]['text'])

    except sr.UnknownValueError:
        st.caption("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        st.caption(f"Error connecting to the recognition service: {e}")
    except openai.error.OpenAIError as e:
        st.caption(f"OpenAI API error: {e}")

    st.divider()
