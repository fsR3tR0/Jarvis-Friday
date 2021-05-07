#! /usr/bin/python3

import speech_recognition as sr
import os 
import playsound
from gtts import gTTS   #beszedhez
import time
import ascii_art as art
import pyttsx3
import subprocess   #ezzel tudunk programokat megnyitni
from datetime import datetime   # pontos ido
import webbrowser
import wikipedia

# flagek a ciklusokhoz, kesobb pontosabb elnevezes
flag = True
flag2 = True
flag3 = True
flag_sleep = False

class OBJ_Time(object):
    def Hours(self):
        self.now = datetime.now()
        self.hors = str(self.now.hour) + ':' + str(self.now.minute) + ':' + str(self.now.second)
        return self.hors

def speak(text):
    tts = gTTS(text = text, lang="en") #hu-it-'fr-fr'-'en-us'
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()

def get_sound():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception '+ str(e))

    return said

def get_sound_sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = r.recognize_google(audio)
        # try:
        #     said = r.recognize_google(audio)
        #     # print(said)
        # except Exception as e:
        #     # print('Exception '+ str(e))
    return said


def write_note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(':','-')+'note.txt'
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["gedit",file_name])
    # subprocess.Popen(["notepad.exe",filename]) ez windows
    # sublime = "/root/Desktop/"
    #linux

def open_note():
    date = datetime.datetime.now()
    file_name = str(date).replace(':','-')+'note.txt'
    # with open(file_name,"w") as f:
    #     f.write(text)
    # subprocess.Popen(["notepad.exe",filename]) ez windows
    # sublime = "/root/Desktop/"
    subprocess.Popen(["gedit",file_name]) #linux

# note("helo,helo")

speak("Hello, i am Friday")
speak("Welcome Sir!") 
helo = OBJ_Time()
print(helo.Hours())
art.render("Welcome",'slant') 
art.render("Mr. Stark",'slant')
speak("Kerdezz tolem valamit") 

while flag:
    text = get_sound()
    if 'hey Friday' in text:
        speak("Yes sir, i'm listen!")
        flag2 = True
        while flag2:
            text = get_sound()
            if 'open YouTube' in text:
                webbrowser.open_new_tab('www.youtube.com')
                speak("Open Youtube")
                flag2 = False
            elif 'search me something' in text:
                speak('On wich platform?')
                sch = get_sound()
                webbrowser.open('https://www.google.com/search?client=firefox-b-e&q='+ str(sch))
            elif 'open Google' in text:
                webbrowser.open_new_tab('www.google.com')
                speak("Open Google")
                flag2 = False
            elif 'note this' in text:
                speak('Speak now sir')
                text = get_sound()
                write_note(text)
                flag2 = False
            elif 'play some music' in text:
                speak('What music do u want?')
                flag3 = True
                text = get_sound()
                # kell meg ide a vegtelen ciklus plus a flagek
                while flag3:
                    text = get_sound()
                    if "play Guns n' Roses" in text:
                        webbrowser.open_new_tab('https://www.youtube.com/watch?v=Rbm6GXllBiw')
                        speak("Here some Guns n' Roses")
                        flag2 = False
                        flag3 = False
                    elif "play retro" in text:
                        webbrowser.open_new_tab('https://www.youtube.com/watch?v=HHGiSmzTrGM')
                        speak("Here Retro remix")
                        flag2 = False
                        flag3 = False
                    elif 'for work' in text:
                        webbrowser.open_new_tab('https://www.youtube.com/watch?v=sdfe7i-qAeY')
                        flag2 = False
                        flag3 = False
                        # will smith chill music 
                    elif 'give me random music' in text:
                        # we
                        pass
                    ##########
            elif 'open Note' in text:
                open_note()
                speak("Open a Note")
                flag2 = False
            elif 'back' in text:
                flag2 = False
            else:
                speak('Sorry sir, i dont understand, please say it again!')
                speak('if want quit Sir, say BACK please, then exit!') 
    elif "what's the time" in text:
        time = str(helo.Hours())
        speak(time)
    elif 'mute' in text:
        speak('Sounds being mute')
        subprocess.run('amixer set Master mute',shell=True)
    elif 'unmute' in text:
        subprocess.run('amixer set Master unmute',shell=True)
        speak('Sounds being unmute')
    elif 'exit' in text:
        flag = False 
        speak('Good bye Sir!')
    elif 'go to sleep' in text:
        flag_sleep = True
        speak('Wake me up if u want something Sir!')
        while flag_sleep:
            sleep = get_sound()
            if 'wake up' in sleep:
                flag_sleep = False
                speak('Good Morning Sir!')

    else:
        speak('Sorry, i dont understand it')


