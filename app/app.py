import pywhatkit as pwk
from time import sleep
from random import choice
import sys
import pyautogui
import pyttsx3

tts = pyttsx3.init()
def speak(text):
    tts.say(text)
    tts.runAndWait()
escolha_inicial = input("What do you want to do? \n1. Send message \n2. Send random message\n3. Spam\n4. Send encrypted message\n5. Exit\n >  ")

if escolha_inicial == "5":
    print('Bye Bye :D')
    sleep(5)
    sys.exit()
