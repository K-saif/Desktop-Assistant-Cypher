import pywhatkit
import wikipedia
import webbrowser
from main import speak

#wikipidia searcgh function
def wikipediaSearch(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("cypher","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

#google searcgh function
def googleSearch(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("cypher","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("no such result on google")

#youtube searcgh function
def youtubeSearch(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("cypher","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.register('chrome', None)
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done")
