import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir!")

    else:
        speak("Good Evening,sir!")

    speak("Hello...I am Raai Haan's personal virtual assistant...My name is Oscar... Sir,Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'who is' in query:
            speak('he is my boss')

        elif 'portfolio' in query:
            speak("finding Raai Haan's Portfolio")
            webbrowser.open("fahadbinabdullah7.github.io/portfolio")



        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("sure sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Okay sir")
            webbrowser.open("google.com")

        elif 'website' in query:
            speak("Searching best website in the world")
            webbrowser.open("rayhan00007.wordpress.com")




        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
