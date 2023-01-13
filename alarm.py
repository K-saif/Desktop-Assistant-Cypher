import datetime
import os 
from main import speak

def Alarm():
    extractedtime = open("Alarm.txt","rt")
    time = extractedtime.read()
    Time = str(time)
    extractedtime.close()

    deletetime = open("Alarm.txt","r+")
    deletetime.truncate(0)
    deletetime.close()

    def ring(time):
        settime = str(time)
        nowtime = settime.replace("cypher","")
        nowtime = nowtime.replace("set an alarm","")
        nowtime = nowtime.replace(" and ",":")
        Alarmtime = str(nowtime)
        print(Alarmtime)
        while True:
            currenttime = datetime.datetime.now().strftime("%H:%M:%S")
            if currenttime == Alarmtime:
                speak("Alarm ringing")
                os.startfile("music.mp3") #You can choose any music or ringtone 
            elif currenttime + "00:00:30" == Alarmtime:
                exit()

    ring(time)