import speech_recognition as sp

listner = sp.Recognizer()

try:
    with sp.Microphone() as source:
        print("I am listining..")
        voice = listner.listen(source)
        text = listner.recognize_google(voice)
        print(text)

except:
    print("Some Error")
    pass


