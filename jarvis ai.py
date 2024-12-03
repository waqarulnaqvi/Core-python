# 3h 50 min
# 1h 10 min+35 min
# 12:00
import datetime#build in module
import os#build in module
import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import wikipedia# pip install wikepedia
import webbrowser #build in module
import smtplib #build in module
engine=pyttsx3.init('sapi5')#it is used to get voice.
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
# print(voices)
# print("Hello world")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <5:
        speak("Good Night")
    elif hour>=5 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis AI,Please tell me how may I help you")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('swhnaqvi786@gmail.com','yourpassword')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

# 11 15
def takecommand():
    # It takes microphone input from the user and returns string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold=250#kitti voice me bole
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please..")
        return "None"
    return query


if __name__=="__main__":
    # speak("Zaamaaan  is dwarf and lean girl")
    Wishme()
    while True:
        query = takecommand().lower()
    #     logic for executing tasks based on query
        results=""
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak(results+" Not found")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube by waqaarul naqvi ai")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            speak("Opening linkedin by waqaarul naqvi ai")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook by waqaarul naqvi ai")
        elif 'open google' in query:
            webbrowser.open_new_tab("Google.com")
            speak("Opening google by waqaarul naqvi ai")
        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")
            speak("Opening stackoverflow by waqaarul naqvi ai")
        elif 'play music' in query:
            music_dir=""
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'my python code' in query:
            runcode="C:\\Users\\HP\\PycharmProjects\\pythonProject\\"
            code=os.listdir(runcode)
            for c in code:
                print(c)
            os.startfile(os.path.join(runcode,code[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S:")
            day=datetime.datetime.now().strftime(":%a")
            print(f"Sir, The time is {strTime} and Day is {day}")
            speak(f"Sir, The time is {strTime} and Day is {day}")

        elif "bye" in query:
            print("Thank you sir IT'S MY HONOUR TO HELP YOU!")
            speak("Thank you sir IT'S MY HONOUR TO HELP YOU!")
            exit()
        elif "open code" in query:
            runcode = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\"

            # code = os.listdir(runcode)
            os.startfile(runcode)
        elif 'email to waqar ul' in query:
            try:
                speak("What should I say?")
                content=takecommand()
                to="syedwaqarul786@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry sir,I am unable to sent this mail!")
                speak("Sorry sir,I am unable to sent this mail!")