import speech_recognition as sr
from googletrans import Translator

# Initialize recognizer
r = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

    try:
        # Convert speech to text
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio")
    except sr.RequestError:
        print("Sorry, the service is not available")




# Initialize translator
translator = Translator()

# English text to translate

# Translate into Hindi
translated = translator.translate(text, src='en', dest='hi')

# Print the translated text
print("Translated text:", translated.text)
