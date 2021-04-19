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
        #     print(text)
            return text.lower()

    except Exception as e :
        print(e)
        pass

# Send Email  
def sendEmail(receiver, subject, message):
        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.starttls()
        # Login with google account 
        mail_server.login('Sender Email', 'Sender Email Password')
        email_info = EmailMessage()
        email_info ['From'] = 'Sender Email'
        email_info ['To'] = receiver
        email_info ['Subject'] = subject
        email_info .set_content(message)
        mail_server.send_message(email_info )

def talkUser(message):
        engine.say(message)
        engine.runAndWait()









    






get_voice()



