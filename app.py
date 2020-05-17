#Import Modules
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


#Initializing speech recog
r = sr.Recognizer()

#Reacord Audio
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
           mother_speak(ask)
        audio = r.listen(source)
        #Initalize voice data
        voice_data =''
        try:
            voice_data = r.recognize_google(audio)
        #If (err)
        except sr.UnknownValueError:
           mother_speak('Sorry, i did not get that')
        #if(err)
        except sr.RequestError:
            mother_speak('Sorry, my speech service is down')
        return voice_data
    
    
def mother_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    
    
    
    
    
def respond(voice_data):
    if 'what is your name' in voice_data:
        mother_speak('My name is mother')    
    if 'what is the name of your creator' in voice_data:
        mother_speak('The name of my creator is seyi js')
    if 'what time is it' in voice_data:
        mother_speak(ctime())
        
    if 'search' in voice_data:
        search= record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        mother_speak('Here is what i found for ' + search)
    
    if 'find location' in voice_data:
        location= record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        mother_speak('Hear is the location of' + location)
    if 'exit' in voice_data:
        exit()
    
time .sleep(1)   
mother_speak('How can I help You')
while 1:
    voice_data = record_audio()
    respond(voice_data)