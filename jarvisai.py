from tkinter import *
import datetime#build in module
import os#build in module
import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import wikipedia# pip install wikepedia
import webbrowser #build in module
import smtplib #build in module
from PIL import ImageTk,Image
from tkvideo import tkvideo

engine=pyttsx3.init('sapi5')#it is used to get voice.
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class GUI_AI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x750")
        self.maxsize(960, 750)
        self.wm_iconbitmap("11.png")
        self.title("Jarvis A.I")

        # Load the background image
        image = Image.open('jarvis__bg.jpg')
        image = image.resize((960, 750))
        photo = ImageTk.PhotoImage(image)

        # Create a Label Widget to display the background image
        bl = Label(self, image=photo )
        bl.place(x=0, y=0, relwidth=1, relheight=1)


    def Wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 5:
            # Label(self,text="Good Night",font="lucida 12 italic",fg="white",bg="green").pack(side=LEFT)
            speak("Good Night")
        elif hour >= 5 and hour < 12:
            # Label(self,text="Good Morning",font="lucida 12 italic",fg="white",bg="green").pack(side=LEFT)
            speak("Good Morning")
        elif hour >= 12 and hour < 18:
            # Label(self,text="Good Afternoon",font="lucida 12 italic",fg="white",bg="green").pack(side=LEFT)
            speak("Good Afternoon")
        else:
            # Label(self,text="Good Evening",font="lucida 12 italic",fg="white",bg="green").pack(side=LEFT)
            speak("Good Evening")

        # Label(text="I am Jarvis AI,Please tell me how may I help you",font="lucida 12 italic",fg="white",bg="green").pack(side=LEFT)
        speak("I am Jarvis AI,Please tell me how may I help you")

    def sendEmail(self,to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('swhnaqvi786@gmail.com', 'yourpassword')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()

    def takecommand(self):
        # It takes microphone input from the user and returns string output.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # Label(text="Listening..",font="lucida 12 bold",fg="white",bg="blue").pack(side=LEFT)
            # r.energy_threshold=250#kitti voice me bole
            r.pause_threshold = 2
            audio = r.listen(source)
        try:
            print("Recognizing...")
            # Label(text="Recognizing..",font="lucida 12 bold",fg="white",bg="blue" ).pack(side=LEFT)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            speak("say that again please..")
            # Label(self,text="say that again please..",font="lucida 12 bold",fg="white",bg="blue").pack(side=LEFT)
            return "None"
        return query


if __name__=="__main__":
    jarvis=GUI_AI()
    jarvis.Wishme()
    # jarvis.config(bg='#39A388')
    # jarvis.mainloop()


    while True:
        query = jarvis.takecommand().lower()
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
            speak("Opening youtube by jarvis ai")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            speak("Opening linkedin by jarvis ai")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook by jarvis ai")
        elif 'open google' in query:
            webbrowser.open_new_tab("Google.com")
            speak("Opening google by jarvis ai")
        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")
            speak("Opening stackoverflow by jarvis ai")
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
                content=jarvis.takecommand()
                to="syedwaqarul786@gmail.com"
                jarvis.sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry sir,I am unable to sent this mail!")
                speak("Sorry sir,I am unable to sent this mail!")