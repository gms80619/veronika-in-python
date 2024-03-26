# veronika-in-python
This is about an AI assistant, Veronika this is like Google Assistant but smart
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Veronika and I am here to help you")

def takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User:", query)
        return query.lower()
    except Exception as e:
        print(e)
        return "None"

if __name__ == "__main__":
    try:
        wishme()
        while True:
            input("Press 'ENTER': ")
            query = takecommand()

            if 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")
                speak("Ok boss")

            elif 'information' in query:
                try:
                    speak("Searching")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("Here is the information I found")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I didn't find any information")
                    print("Sorry, I didn't find any information")

            elif 'hello' in query:
                speak("Hello, how can I help you?")

            elif 'hi' in query:
                speak("Hi!")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")
                speak("Ok boss")

            elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com")
                speak("Ok boss")

            elif 'open amazon' in query:
                webbrowser.open("https://www.amazon.in")
                speak("Ok boss")

            elif 'open flipkart' in query:
                webbrowser.open("https://www.flipkart.com")
                speak("Ok boss")

            elif 'open aliexpress' in query:
                webbrowser.open("https://www.aliexpress.com")
                speak("Ok boss")

            elif 'music' in query:
                speak("Playing music")
                # Modify the music_dir to your music folder path
                music_dir = 'C:\\path\\to\\music\\folder'
                songs = os.listdir(music_dir)
                song = os.path.join(music_dir, random.choice(songs))
                os.startfile(song)

            elif 'open terminal' in query:
                os.system("start cmd")
                speak("Ok boss")

            elif 'love you' in query:
                speak("Thank you, I respect you too")

            elif 'what can you do' in query:
                speak("I can play music, open YouTube, open Google, and many more things for you")

            elif 'why sorry' in query:
                speak("I failed to do that")

            elif 'play another song' in query or 'play song which I want' in query:
                speak("You can do that in the app")
                webbrowser.open("https://www.gaana.com")

            elif 'my location' in query:
                webbrowser.open("https://www.google.com/maps")
            
            # Add other commands as needed...

    except Exception as e:
        print(f"Oops! Something went wrong... \n {e}")
