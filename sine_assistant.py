import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('i am your nitish')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'saini' in command:
                command= command.replace('saini','')
                print(command)
    except:
        pass
    return command
def run_saini():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is '+ time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is','')
        info = wikipedia.summary(thing,1)
        print(info)
        talk(info)
    elif 'where is ' in command:
        area = command.replace('where is','')
        info = wikipedia.summary(area,1)
        print(info)
        talk(info)
while True:
    run_saini()

