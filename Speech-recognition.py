import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
import webbrowser
import time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Sky_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Sky_speak('sorry, i did not understand')
        except sr.RequestError:
            Sky_speak('sorry my speech service is down')
        return voice_data

def Sky_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'Hey Sky' in voice_data:
        Sky_speak('How may i be of use')
    if 'What time is it' in voice_data:
        Sky_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Sky_speak('Here is what i found for ' + search)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)