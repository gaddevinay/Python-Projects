import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
import json
import smtplib
import os
import time
import subprocess
import cv2
from datetime import datetime


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',100)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id )

# API keys and email credentials
WEATHER_API_KEY = "03b5725aa4e9e161704eb048fdd10e60"
NEWS_API_KEY = "4939b6b32cfa4a9bb6dc36ffca2c9c26"
GMAIL_USERNAME = "jarvis.ai.jarvis@gmail.com"
GMAIL_PASSWORD = "caat jkty mrps dnex"

def talk(text):
    engine.say(text)
    engine.runAndWait()
def print_talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    command="nothing speaked"
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print('you : ',command)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        pass
    return command

def greet_user():    
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        talk(f"Good Morning Sir")
    elif (hour >= 12) and (hour < 17):
        talk(f"Good afternoon Sir")
    else:
        talk(f"Good Evening Sir")
    talk(f"I am Jarvis. Please tell me how can i help you sir?")
def get_weather_info(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    talk(f"The current temperature is {temperature}, but it feels like {feels_like}")
    talk(f"Also, the weather report talks about {weather}")
    talk("For your convenience, I am printing it on the screen sir.")
    print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

    
def get_news_headlines():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    for i in range(3):
        title = data['articles'][i]['title']
        print_talk(f"Headline number {i+1}: {title}")

def send_email(to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(GMAIL_USERNAME, to, message)
        print_talk("Email sent successfully!")
    except Exception as e:
        talk("Sorry, I couldn't send the email. Please try again later.")
        print(e)

def translate_text(text, source_language, target_language):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language}&tl={target_language}&dt=t&q={text}"
    response = requests.get(url)
    data = json.loads(response.text)
    translated_text = data[0][0][0]
    talk(f"The translated text is {translated_text}")
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)

def run_jarvis():
    command = take_command()
    if 'play' in command or 'play song' in command:
        song = command.replace('play song', '').replace('play', '').strip()
        talk('Playing song ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'are you there' in command:
        talk("Yes Sir, at your service")
    elif 'who made you' in command:
        talk("Yes Sir, Vinay build me in AI, My name is Jarvis")
    elif 'who is the' in command or 'who is' in command :
        person = command.replace('who is the', '').replace('who is','').strip()
        info = wikipedia.summary(person, 1)
        print_talk(info)
    elif 'send message' in command or 'whatsapp message' in command:
        talk('What should i send')
        message=take_command()
        talk('Please say recipient number sir')
        number=take_command()
        send_whatsapp_message(number, message)
    elif 'open camera' in command:
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif 'close camera' in command:
        subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    elif 'open google' in command or 'open chrome' in command:
        url = 'http://www.google.com'
        webbrowser.open_new(url)
    elif 'open youtube' in command:
        url = 'https://www.youtube.com'
        webbrowser.open_new(url)
    elif 'open calculator' in command or 'open calci' in command:
        subprocess.Popen('calc.exe')
    elif 'open insta' in command:
        url = 'https://www.instagram.com/'
        webbrowser.open_new(url)
    elif 'open facebook' in command:
        url = 'https://www.facebook.com/'
        webbrowser.open_new(url)
    elif 'search in google' in command or 'search on google' in command:
        talk("What do you want to search sir")
        while True:
            search_query = take_command()
            if search_query!='nothing speaked':
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open_new_tab(url)
                break
    elif 'search in youtube' in command or 'search on youtube' in command:
        talk("What do you want to search sir")
        while True:
            search_query = take_command()
            if search_query!='nothing speaked':
                url = f"https://www.youtube.com/results?search_query={search_query}"
                webbrowser.open_new_tab(url)
                break
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather in' in command:
        city = command.replace('weather in', '')
        get_weather_info(city)
    elif 'news' in command:
        get_news_headlines()
    elif 'email' in command or 'mail' in command:
        try:
            while True:
                talk("What should I say?")
                body = take_command()
                if body!='nothing speaked':
                    talk("Enter recipient email address: ")
                    recipient = input("Enter recipient email address: ")
                    send_email(recipient, "Jarvis", body)
                    break
        except Exception as e:
            talk("Sorry, I couldn't send the email. Please try again later.")
            print(e)
    elif 'translate' in command:
        try:
            talk("What should I translate?")
            text = take_command()
            talk("What is the source language?")
            source_language = take_command()
            talk("What is the target language?")
            target_language = take_command()
            translate_text(text, source_language, target_language)
        except Exception as e:
            talk("Sorry, I couldn't translate the text. Please try again later.")
            print(e)
    elif 'shutdown' in command:
        talk("Goodbye!")
        os.system("shutdown /s /t 1")
    elif 'nothing speaked' in command:
        print('Nothing Speaked')
    elif 'exit' in command or 'goodbye' in command:
        print('Exiting.')
        talk("Goodbye!Sir, if you require any further assistance, do not hesitate to ask. Farewell!")
        return False
    else:
        talk('Sir, Please say the command again.')
greet_user()
while True:
    command_result = run_jarvis()
    if command_result == False:
        break

    
