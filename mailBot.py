import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sp.Recognizer()
engine = pyttsx3.init()

# for index, name in enumerate(sp.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# mic =sp.AudioFile('./audio/pzm12.wav')
mic = sp.Microphone()

def get_voice():
    with mic as source:
            print("I am listining..")
            audio = listener.listen(source)
    try:
            text = listener.recognize_google(audio)
            print(text)
            # return text.lower()

    except Exception as e :
        print(e)
        pass

# Get Email Information to be send 
def getEmail_Info():

    






get_voice()



