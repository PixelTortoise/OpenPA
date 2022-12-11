# Import required modules 
import speech_recognition as sr
import pyttsx3
import sys
import os

paConfig = ''
openConfig = []

try:
    configTxt = open('config.txt', 'r')
    paConfig = configTxt.readlines()
    configTxt.close()

    openTxt = open('open.txt', 'r')
    rawOpenConfig = openTxt.readlines()
    for i in rawOpenConfig:
        openConfig.append(i.replace(r'\n', ''))
    openTxt.close

except:
    configTxt = open('config.txt', 'w')
    configTxt.write('name=jarvis')
    configTxt.close

    openTxt = open('open.txt', 'w')
    openTxt.close

    print('Config txts generated, fill them out and press enter to close the program')
    cont = input()
    sys.exit

progName = paConfig[0].replace('name=', '') + ' '


# Initialize the recognizer
rec = sr.Recognizer()

def speakText(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognizeMic():

    with sr.Microphone() as source:
        try:

            rec.adjust_for_ambient_noise(source, duration=0.2)
            audio = rec.listen(source)

            inpText = rec.recognize_google(audio)
            inpText = inpText.lower()

            return inpText

        except sr.RequestError as e:
            print('Could not request results; {0}'.format(e))

        except sr.UnknownValueError:
            print('Unknown error occured')

while(True):

    inp = recognizeMic()

    if inp is not None:

        if inp.startswith(progName):

            inp = inp.replace(progName, '')

            if inp == 'exit program':
                speakText('confirm close?')

                inp = recognizeMic()

                if inp == 'yes':
                    speakText('closing')
                    sys.exit()

                else:
                    speakText('not closing')

            if inp.startswith('open'):
                inp = inp.replace('open ', '')
                repeats = 0

                for i in openConfig:
                    repeats += 1
                    if inp in i:
                        
                        inp2 = openConfig[repeats-1]

                speakText('opening {}'.format(inp))
                inp2 = inp2.replace('{}='.format(inp), '')

                os.system(inp2)
                