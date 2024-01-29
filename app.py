from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define the available voices
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
print("Available voices:", ", ".join(voices))

while True:
    selected_voice = input("Please select a voice from the above options: ").lower()
    if selected_voice in voices:
        break
    else:
        print("Invalid voice selection. Please choose a valid option.")


# List of supported languages
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

# Get user input for the language
selected_language = input("Please enter the language for your text: ").capitalize()

# Get user input for the TTS
user_input = input("Please enter the text you want to convert to speech: ")

try:
    # Create the speech response
    response = client.audio.speech.create(
        model="tts-1",
        voice=selected_voice,
        input=user_input,
    )

    # Save the response content to a file
    with open("output.mp3", "wb") as file:
        file.write(response.content)
    print("Audio file has been created as 'output.mp3'")

except Exception as e:
    print(f"An error occurred: {e}")

