import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_notes():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening... Please start speaking.")
        print("Listening...")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            with open("voice_notes.txt", "a") as f:
                f.write(text + "\n")

            speak("Note saved successfully.")

        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            print("Sorry, I did not understand that.")

        except sr.RequestError as e:
            speak("Could not request results; check your internet connection.")
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    take_notes()
