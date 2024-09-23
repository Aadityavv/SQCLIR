import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio")
    except sr.RequestError:
        print("Sorry, the service is not available")

translator = Translator()

translated = translator.translate(text, src='en', dest='hi')

print("Translated text:", translated.text)

language = 'hi'
speech = gTTS(text=translated.text, lang=language, slow=False)
speech.save("output.mp3")
os.system("start output.mp3")