import streamlit as st
from gtts import gTTS

def text_to_speech(text):
    # Create a text-to-speech object
    tts = gTTS(text=text, lang='en')
    # Save the audio file
    tts.save('output.mp3')

    # Play the audio file
    #os.system('mpg321 output.mp3')

    # Save the audio file as a bytes object
    #audio_bytes = tts.get_audio_bytes()

    # Play the audio file
    st.audio("output.mp3")

# Call the text-to-speech function with some text
text_to_speech("Hello, how can I assist you?")
