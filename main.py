import pyttsx3
import speech_recognition
import datetime
import os 
import pyautogui

#creating an engine for voice 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id) # you can change assistant voice by changing the number
rate = engine.setProperty("rate",170) 

# speak function of assistant 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# for listning or taking command
def takeCommand():
	r = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print(e)
		print("Unable to Recognize")
		return "None"
	return query

# function for alarm 
def alarm(query):
    timehere = open("Alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# main loop 
if __name__ == "__main__":
        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                from greet import greet
                greet()

                while True:
                    query = takeCommand().lower()
#conversation
                    if "hello" in query:
                        speak("Hello, how are you ?")
                    
                    elif "i am fine" in query:
                        speak("that's great")
                    
                    elif "how are you" in query:
                        speak("Perfect")
                   
                    elif "thank you" in query:
                        speak("you are welcome")

                    elif "who made you" in query or "who created you" in query:
                        speak("I have been created by saif khan")

                    elif "go to sleep" in query:
                        speak("Ok, You can me call anytime")
                        break
                    #you can create more conversations in this loop 

# basic functions for playing video                      
                    elif "pause" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    
                    elif "play" in query:
                        pyautogui.press("k")
                        speak("video played")
                    
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")

                    elif "volume up" in query:
                        from keyboard import volumeup
                        speak("Turning volume up")
                        volumeup()
                    
                    elif "volume down" in query:
                        from keyboard import volumedown
                        speak("Turning volume down")
                        volumedown()  

#open and close apps
                    elif "open" in query:
                        from autoapps import openapp
                        openapp(query)
                    elif "close" in query:
                        from autoapps import closeapp
                        closeapp(query)

### for search or brows
                    elif "google" in query:
                        from Search import googleSearch
                        googleSearch(query)
                    
                    elif "youtube" in query:
                        from Search import youtubeSearch
                        youtubeSearch(query)
                    
                    elif "wikipedia" in query:
                        from Search import wikipediaSearch
                        wikipediaSearch(query)
                   
#### set alarm ####
                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done")

#current time
                    elif "waht is the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"the time is {strTime}")

#remember                             
                    elif "remember that" in query:
                        rememberMsg = query.replace("remember that","")
                        rememberMsg = query.replace("cypher","")
                        speak("You told me to remember that"+rememberMsg)
                        remember = open("Remember.txt","a")
                        remember.write(rememberMsg)
                        remember.close()
                    
                    elif "what do you remember" in query:
                        remember = open("Remember.txt","r")
                        speak("You told me to remember that" + remember.read())

#### news #####
                    elif "news" in query:
                        from NewsRead import latestnews
                        latestnews()

#### calculate ####
                    elif "calculate" in query:
                        from Calculatenumbers import Apis
                        from Calculatenumbers import Calc
                        query = query.replace("calculate","")
                        query = query.replace("cypher","")
                        Calc(query)

#spellChecker                  
                    elif "spelling check" in query:
                        from SpellChecker import check_spell
                        check_spell()
                        
#wahtsapp
                    elif "whatsapp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()
#sleep
                    elif "finally sleep" in query:
                        speak("Going to sleep")
                        exit()

#shutdown
                    elif "shutdown the system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")

                        elif shutdown == "no":
                            break
