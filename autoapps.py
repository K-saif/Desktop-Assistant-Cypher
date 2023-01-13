import os 
import pyautogui
import webbrowser
from time import sleep
from main import speak

#creating dictionary for apps 
autoapps = {"chrome":"chrome","vscode":"code","commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","powerpoint":"powerpnt","calender":"calender"}

#creating function to open apps
def openapp(query):
    speak("Launching")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("cypher","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(autoapps.keys())
        for app in keys:
            if app in query:
                os.system(f"start {autoapps[app]}")

#creating function to close tabs 
def closeapp(query):
    speak("Closing")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")
# we can create for n number of tabs


#creating function to close apps
    else:
        keys = list(autoapps.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {autoapps[app]}.exe")
