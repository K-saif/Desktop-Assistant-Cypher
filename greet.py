import datetime
from main import speak

#function for grteeting
def greet():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour >12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("How can I help you ?")