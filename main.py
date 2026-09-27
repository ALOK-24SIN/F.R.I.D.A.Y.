import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://gemini.google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

if __name__ == "__main__":
    speak("Initializing friday....")
    while True:
        # listen for the wake word "F.R.I.D.A.Y."
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=10)

       
        print("Recognizing...")
        #recogniz speech using google
        try:
           command = r.recognize_google(audio)
           print(command)
        except sr.UnknownValueError:
            print("Google could not understand audio")
            if(command.lower() == "friday"):
                speak("Yes karan")
                #listen for command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, phrase_time_limit=10)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error;{0}.format(e)")
                