import pywhatkit as pwk
from time import sleep
from random import choice
import sys
import pyautogui
import pyttsx3
import webbrowser
#import hashlib

#functions
tts = pyttsx3.init()
def speak(text):
    tts.say(text)
    tts.runAndWait() 
def encrypt(msg):
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
def spammer(text, reapeter, delay):
    i = 0
    j = 30
    webbrowser.open_new_tab('web.whatsapp.com')
    print("Choose the contact do you want to spam")
    while i <= j:
        sleep(1)
        print(f'Counter: {i}')
        speak(i)
        i += 1
    for a in range(reapeter):
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        pyautogui.sleep(delay)
        print(f'You sent {a} messages')
    speak('Finished')
    print('Finish')
def send_random_msg():
    def random_msg():
        msgs = ['Hi', 'Hello', 'Funny', 'Thanks', 'I love you', 'Wtf', 'Jesus christ', 'Fuck', 'Smurfs', 'Potato', 'Tomato', 'Juice', 'Orange', 'Apple', 'Microsoft', 'Linux', 'Is better', 'Shit', '...']
        random_msg_choice = choice(msgs)
        return random_msg_choice
    user_phone_number = input("User phone number\n >  ")
    msg_hour = int(input("Hour the message will be sent\n >  "))
    msg_min = int(input("Minute the message will be sent\n >  "))
    msg_delay = int(input("Message sent delay\n >  "))
    send_msg(user_phone_number, random_msg(), msg_hour, msg_min, msg_delay)
#inputs and verifications
escolha_inicial = input("What do you want to do? \n1. Send message \n2. Send random message\n3. Spam\n4. Send encrypted message\n5. Exit\n >  ")

if escolha_inicial == "5":
    print('Bye Bye :D')
    sleep(5)
    sys.exit()
elif escolha_inicial == "4":
    cipher_text = input("Your message here\n >  ")
    encrypt(cipher_text)
elif escolha_inicial == "1":
    
    send_msg()
elif escolha_inicial == "3":
    spam_delay = int(input("Messages delay\n >  "))
    spam_content = input("Message do you want to spam\n >  ")
    spam_reapeter = int(input("How many times do you want to sent\n >  "))
    spammer(spam_content, spam_reapeter, spam_delay)
elif escolha_inicial == "1":
    user_phone_number = input("User phone number\n >  ")
    msg_content = input("Your message here\n >  ")
    msg_hour = int(input("Hour the message will be sent\n >  "))
    msg_min = int(input("Minute the message will be sent\n >  "))
    msg_delay = int(input("Message sent delay\n >  "))
    send_msg(user_phone_number, msg_content, msg_hour, msg_min, msg_delay)
elif escolha_inicial == "2":
    send_random_msg()
else:
    print(f'{escolha_inicial} is invalid')
print("End of the script")
sys.exit()
