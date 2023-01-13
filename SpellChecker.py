import time
from textblob import TextBlob
from main import speak

# function for checking spelling 
def check_spell():
    speak('enter the word')	
    a =input('enter words:')	
    time.sleep(1)
    speak('did you mean')
    print("original text: "+str(a))

    b = TextBlob(a)

    # prints the corrected spelling
    print("corrected text: "+str(b.correct()))
    speak(str(b.correct()))
