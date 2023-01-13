import wolframalpha
from main import speak

# function for APi 
def Apis(query):
    apikey = "RA8PAE-22VJW4VV8Q"  #API key for calculator
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

# function for calculator
def Calc(query):
    Term = str(query)
    Term = Term.replace("cypher","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = Apis(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")