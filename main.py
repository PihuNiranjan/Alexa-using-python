import pywhatkit
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

"""SET VOICE MALE OR FEMALE"""

voices  = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)       # voices[0].id ---> male voice
engine.setProperty('voice', voices[1].id)         # voices[1].id ---> female voice

""" SET VOLUME """

volume = engine.getProperty('volume')             #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0) 

"""TEXT TO SPEECH"""

def talk(text):
    engine.say(text)
    engine.runAndWait()

""" SPEECH TO TEXT """
def talk_command():
    try:
        with sr.Microphone() as source:
            print('\nListening....')
            # print("Adjusting noise...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source,timeout=5)
            print("Done recording.")
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command :
                command = command.replace('alexa', '')
                print(command)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
    return command

def main():
    intro = "Hello! I am Alexa. How can i help you ?"
    talk(intro)
    song = talk_command()
    try: 
        pywhatkit.playonyt(song)
        talk(song) 
        print(f"\nPlaying... {song}")   
    except:        
        print("Network Error Occurred")


main()