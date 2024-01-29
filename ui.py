import streamlit as st
import requests
import os
from openai import OpenAI

# Initialize the OpenAI client with your API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("Please provide the OpenAI API key as an environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

# Streamlit UI
st.title('Text-to-Speech Application')

# Dropdown for voice selection
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
selected_voice = st.selectbox("Select a Voice", voices)

# Dropdown for language selection
languages = [
     "Afrikaans", "Arabic", "Armenian", "Azerbaijani", "Belarusian", "Bosnian", "Bulgarian",
    "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", 
    "Finnish", "French", "Galician", "German", "Greek", "Hebrew", "Hindi", "Hungarian", 
    "Icelandic", "Indonesian", "Italian", "Japanese", "Kannada", "Kazakh", "Korean", 
    "Latvian", "Lithuanian", "Macedonian", "Malay", "Marathi", "Maori", "Nepali", "Norwegian", 
    "Persian", "Polish", "Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", 
    "Spanish", "Swahili", "Swedish", "Tagalog", "Tamil", "Thai", "Turkish", "Ukrainian", 
    "Urdu", "Vietnamese", "Welsh"
]
selected_language = st.selectbox("Select a Language", languages)

# Text input for TTS
user_input = st.text_area("Enter the Text")

# Button to generate speech
if st.button('Convert to Speech'):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice=selected_voice,
            input=user_input,
        )

        # Save the response content to a file
        file_path = "output.mp3"
        with open(file_path, "wb") as file:
            file.write(response.content)
        st.success("Audio file has been created")

        # Display audio file
        st.audio(file_path)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Add custom CSS for footer
footer_style = """
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 10px;
background-color: rgba(255, 255, 255, 0.5);  /* Semi-transparent light background */
color: #000;                                  /* Dark text for visibility */
border-top: 1px solid #000;                   /* Border to distinguish the footer */
z-index: 1000;                                /* Ensures it stays on top of other elements */
"""

# Footer
st.markdown(
    '<div style="{}">Developed by Mirac.eth<br>Contact: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)
