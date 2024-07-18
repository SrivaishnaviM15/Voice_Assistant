#!/usr/bin/env python
# coding: utf-8

# In[13]:


import subprocess
import wolframalpha
import pyttsx3
import tkinter
import operator
import smtplib
import getpass
from email.message import EmailMessage
import json
import speech_recognition as sr
from datetime import *
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import time
import requests
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from ecapture import ecapture as ec


# In[14]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# In[17]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def username():
    assname =("Digie Bud")
    speak(f"Hello!  I am your Assistant {assname}")
    speak("How may I address you")
    urname = takeCommand()
    speak(f"Welcome ,{urname}")
    print("Welcome",urname)
    speak(f"How may i assist you, {urname}")
   

def takeCommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-us')
        print(f"User said: {query}\n")
    except Exception as e:       
        print(e)   
        print("Unable to Recognize your voice.") 
        return "Buddy"
       
    return query

def wishMe():
    hour = int(datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Bud !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Bud !")  
  
    else:
        speak("Good Evening Bud !") 

def sendemail(subject,to_address,message):
    smtp1=smtplib.SMTP('smtp-mail.outlook.com',587)
    smtp1.ehlo()
    smtp1.starttls()
    email=input("Enter your mail id:")
    password=getpass.getpass("Enter your password:")
    smtp1.login(email,password)
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject']=subject
    smtp1.sendmail(email,to_address,msg.as_string())        


# In[18]:


clear = lambda: os.system('cls')
clear()
wishMe()
username()
while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\akash\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'time' in query:
            Time=datetime.now()
            speak("Sir, the time is")
            speak(f"{Time.hour} hours")
            speak(f"{Time.minute} minutes")
            speak(f"and{Time.second} seconds")
    
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, mate")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            break
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ,well thats classified information.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
        elif "calculate" in query:
             
            app_id = "AQYGXY-H6HH367V8X"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who am i" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to CBIT. further It's a secret")
 
     
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")
 
        elif 'reason for you' in query:
            speak("I was created as a EE Project,the rest is classified wink wink ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")
 

 
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want me to stop listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/"+location)
            
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "DIGI Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('digi.txt', 'w')
            file.write(note)
            
         
        elif "show the note" in query or "read the note" in query:
            speak("Showing Notes")
            file = open("digi.txt", "r")
            print(file.read())
            speak(file.read())
 
                     
        elif "digi bud" in query:
             
            wishMe()
            speak("digi bud in your service Mister")
            speak(assname)
 
        elif "weather" in query:
           
            api_key = "4a759341da3376d478b606f2e2b2b61c"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "q=" + city_name + "&APPID=" + api_key
            response = requests.get(complete_url)
            x = response.json()
             
               
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " +str(weather_description))
            speak(f"Current Temperature is {current_temperature},Current Humidity is {current_humidity},current pressure is {current_pressure}and description is {weather_description}")
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apikey=5fcb732b78b34006a282c1a0f218d8e0''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news of india')
                print('''=============== NEWS ============'''+ '\n')
                 
                for item in data['articles']:
                    if i<6: 
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                    else:
                        break
            except Exception as e:
                 
                print(str(e))    
             

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        
        elif "email" in query:
            speak("Please provide the subject of your message")
            subject=takeCommand()
            speak("Please convey the message you want to send")
            message=takeCommand()
            speak("Whom should I send this message")
            to_address=input("Enter recipient mail id:")
            speak("Please provide your login credentials")
            sendemail(subject,to_address,message)
            speak("Email has been sent !")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Buddy")
            speak(assname)
 
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you asked that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
             
            
            client = wolframalpha.Client("4a759341da3376d478b606f2e2b2b61c")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")    
         


# In[ ]:





# In[ ]:




