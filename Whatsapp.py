import pywhatkit
import datetime
from datetime import timedelta
from datetime import datetime
from main import speak


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    a = int(input('''majid - 1
                   gauresh - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+919146222412",message,time_hour=strTime,time_min=update)
        
    elif a==2:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+919554261153",message,time_hour=strTime,time_min=update)

        # you can write n numbers of contacts in this if eles condition  