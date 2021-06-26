import pywhatkit as pwk
from time import sleep
from random import choice
import sys
import pyautogui
import pyttsx3

#functions
tts = pyttsx3.init()
def speak(text):
    tts.say(text)
    tts.runAndWait() 
def cesar(msg):
    cipher_key = int(input("Caesar cipher key\n >  "))
    user_phone_number = input("User phone number\n >  ")
    msg_hour = int(input("Hour the message will be sent\n >  "))
    msg_min = int(input("Minute the message will be sent\n >  "))
    msg_delay = int(input("Message sent delay\n >  "))
    resultado = ''
    for i in range (0, len(msg)):
        resultado = resultado + chr(ord(msg[i]) + cipher_key)
    speak(resultado)
    print(f'\n{resultado}')
    sleep(0.25)
    send_msg(user_phone_number, resultado, msg_hour, msg_min, msg_delay)    
def send_msg(phone_n, content, h, m, wt):
    sleep(0.25)
    pwk.sendwhatmsg(phone_n, content, h, m, wt)
#inputs and verifications
escolha_inicial = input("What do you want to do? \n1. Send message \n2. Send random message\n3. Spam\n4. Send encrypted message\n5. Exit\n >  ")

if escolha_inicial == "5":
    print('Bye Bye :D')
    sleep(5)
    sys.exit()
elif escolha_inicial == '4':
    cipher_text = input("Your message here\n >  ")
    cesar(cipher_text)
else:
    print(f'{escolha_inicial} is invalid')