import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

#def talk(words):
 #   print(words)
  #  os.system("say " + words)

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Привет, спроси у меня что-либо")

#talk("こんにちは、何か聞いてください")
#talk("Kon'nichiwa, nanika kiitekudasai")
#talk("Hi, ask me something")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    if 'open website' in zadanie:
        talk("Уже открываю")
        url = 'https://itproger.com'
        webbrowser.open(url)
    elif 'name' in zadanie:
        talk("Меня зовут Сири")
    elif 'stop' in zadanie:
        talk("Да, конечно, без проблем")
        sys.exit()

while True:
    makeSomething(command())