import datetime
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Finder, please tell me how can I help you")


def textCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        speak("please say that again")
        return "none"
    return query


wish()

while True:
    query = textCommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'my name' in query:
        speak("Your name is ayon")
        print(speak)
    elif 'time' in query:
        hour = str(int(datetime.datetime.now().hour))
        min = str(int(datetime.datetime.now().minute))
        time = (hour+"hours"+min+"minutes")
        speak(time)
    elif 'the date' in query:
        date = str(int(datetime.datetime.now().day))
        mon = str(datetime.datetime.now().month)
        year = str(int(datetime.datetime.now().year))
        speak(date)
        speak(mon)
        speak(year)
    elif 'your name' in query:
        speak("My name is Finder")
        print(speak)
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'tomorrow' in query:
        date = str(int(datetime.datetime.now().day) + 1)
        speak(date)
    elif 'is this a leap year' in quary:
        year = int(datetime.datetime.now().year)
        l = year % 4
