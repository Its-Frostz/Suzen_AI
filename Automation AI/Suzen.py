


#                                                                    Please at first read the README file



from selenium import webdriver #read the readme file
import pyautogui #pip install pyautogui
import time
import keyboard #pip install keyboard
import random 
import pyttsx3 #pip install pyttsx3 and then if you get an error please read the readme file
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


# Setting up the voice output

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# A function to wish when the program first starts and respective to the time

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   

    else:
        speak("Good Evening sir")  

    speak("Please tell me how may i help you")  

#It takes microphone input from the user and returns string output

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pyautoguiuse_threshold = 0.75
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception: 
        print("Say that again please...")  
        return "None"
    return query

a = 1

if __name__ == "__main__":
    wishMe()
    while a == 1:
        query = takeCommand().lower()
        
#         wikipedia search

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # web_browser search

        elif 'search' in query:

            query = query.replace("search", "")
            query = query.replace("search for", "")
            search_string = query
            speak('searching' + search_string)

            webdriver = "# Webdriver path here" # Downloading webdriver is required, check readme if u don't know how to do so
            browser = webdriver.Chrome(webdriver)
            for i in range(1): 
                matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
            
       # play a song

        elif 'play' in query:

            if 'on youtube' in query:
                query = query.replace("on youtube", "")
                search_string = query
                speak('trying to play' + search_string)

                # Point(x=464, y=525) first video
                webdriver = "# Webdriver path here"
                browser = webdriver.Chrome(webdriver)
                for i in range(1):
                    matched_elements = browser.get("https://www.youtube.com/search?q=" + search_string + "&start=" + str(i))
                time.sleep(1)
                pyautogui.moveTo(505, 457, duration=0.2)#(x=505, y=457) values for youtube first video in 1080pscreen
                pyautogui.click()
            
            else:
                search_string = query
                pyautogui.keyDown('winleft')
                pyautogui.press('d')
                pyautogui.keyDown('winleft')
                pyautogui.keyDown('winleft')
                pyautogui.press('s')
                pyautogui.keyDown('winleft')
                pyautogui.keyDown('winleft')
                pyautogui.press('s')
                pyautogui.keyUp('winleft')
                pyautogui.typewrite("spotify")
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(2.25)
                tempo=1
                while tempo == 1:
                    if pyautogui.locateOnScreen("#path here",confidence=0.6) != None:
                        tempo = 2
                    else:
                        time.sleep(0.5)
                tempo = 1
                pyautogui.click(x=88, y=121)#For 1080p screens only
                time.sleep(0.2)
                pyautogui.click(x=809, y=33)#For 1080p screens only
                pyautogui.typewrite(search_string)
                time.sleep(1)
                while tempo==1:
                    if pyautogui.locateOnScreen("path here", confidence=0.8) != None:
                        tempo = 2
                    else:
                        time.sleep(0.5)
                tempo = 1
                pyautogui.moveTo(862, 176)#For 1080p screens only
                time.sleep(0.4)
                pyautogui.click()#For 1080p screens only
        
        # simple time

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # Switch between apps

        elif 'switch window' in query:
            pyautogui.keyDown('altleft')
            pyautogui.press('tab')
            pyautogui.keyUp('altleft')
  
        # Minimize current application
    
        elif 'minimize current' or 'minimize this' in query:
            pyautogui.keyDown('winleft')
            pyautogui.press('down')
            pyautogui.keyUp('winleft')
  
        # Minimize all apps and go to home screen

        elif 'minimize' in query:
            pyautogui.keyDown('winleft')
            pyautogui.press('d')
            pyautogui.keyUp('winleft')

        # opening applications

        elif 'open' in query:
            search_string = query.replace("open", "")    
        
            speak('opening ' + search_string)
            pyautogui.keyDown('winleft')
            pyautogui.press('s')
            pyautogui.keyUp('winleft')
            pyautogui.typewrite(search_string)
            time.sleep(0.2)
            pyautogui.press('enter')
                
        # chatbot (I may have been a little childish here plz ignore:) )

        elif 'can i ask a question' in query:
            speak('definatly sir go ahead')

        elif 'whats your name' in query or 'who are you' in query:
            speak("hallo, my name is suzen i am an artificial intellegence")

        elif 'nothing else thank you' in query or 'thanks for the compliment' in query or 'thank you' in query or 'thanks' in query or 'thanks a lot' in query:
            # print("you are welcome sir, feel free to come to me whenever you need me")
            speak("you are welcome sir")

        elif 'i did it' in query:
            speak('congratulation sir, i am glad to hear that')

        elif 'what can you do' in query:
            speak("I can besiclly do any-thing you say. I can search, for any information, launch any application, automate anything, can serve you as a chat bot, play music, set alarms, help you in your work and do work if u specify the time to automatically do it")

        elif 'morning' in query or 'afternoon' in query or 'evening' in query:
            speak('What shall i do for you sir')

        elif 'how are you' in query:
            speak('I am great sir, what about you')

        elif 'talk' in query or 'no work' in query:
            speak('thats sounds great to me, how are you sir')

        elif 'just fine' in query:
            speak('why just fine sir. why not great')

        elif 'introduction' in query:
            speak('well then, hay there ,i am suzen, an arti-ficial intelligence, made by a-tif')

        elif 'not that great' in query:
            speak('would playing a song make u feel better')

            opinian = takeCommand().lower()
            
            if 'yes' or 'might be' in opinian:
                b = random.randint(0, 9)
                speak('ok sir playing a song from your favourite list')
                music_dir = '#path here'
                song = os.listdir(music_dir)
                os.startfile(os.pyautoguirty.join(music_dir, song[b]))
            
            elif 'no' in opinian:
                speak('ok sir, then shall i open visual studio, codeing might make feel better')

                opinian2 = takeCommand().lower()

                if 'ok' in opinian2:
                    speak('opening code')
                    codepyautoguith = "#path here"
                    os.startfile(codepyautoguith)

                elif 'no' in opinian2:
                    speak('ok sir i wont do that')
                    
        elif 'great' in query:
            speak('glad to hear that')

        elif 'How are you' in query:
            speak('I am doing great')

        elif 'who made you' in query:
            print('Hey there my friend, i am Kronos/Atif😈')
            speak('i am created by Kronos')

        elif 'stop' in query or 'i am done' in query:
            speak('closing')
            a = 2

        
