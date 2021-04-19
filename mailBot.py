import speech_recognition as sp

listener = sp.Recognizer()

# for index, name in enumerate(sp.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# mic =sp.AudioFile('./pzm12.wav')
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
# def getEmail_Info():
    


get_voice()



