import requests
import json
from main import speak

def latestnews():
    #creating a dictionay of different fields in news
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ba19c7bc2c304ee4bb563c5bb82e9de6"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")