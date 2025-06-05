import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech rate

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""

def run_assistant():
    command = listen()

    if "hello" in command:
        talk("Hello! How can I help you?")
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk(f"Today is {date}")
    elif "search" in command:
        search_query = command.replace("search", "")
        talk(f"Searching for {search_query}")
        pywhatkit.search(search_query)
    elif "your name" in command:
        talk("I am your voice assistant.")
    elif "exit" in command or "stop" in command:
        talk("Goodbye!")
        exit()
    else:
        talk("Sorry, I didn't understand that.")

if __name__ == "__main__":
    talk("Hi! I am your Python assistant.")
    while True:
        run_assistant()
