'''
authors: Los-had, lind0-oss
repository: https://github.com/Los-had/whatsapp-automation
license: MIT
'''

from sqlite3.dbapi2 import connect
import pywhatkit as pwk
from time import sleep
from random import choice
import sys
import pyautogui
import pyttsx3
import webbrowser
import sqlite3
from sqlite3 import Error
import speech_recognition as sr
import getpass
import colorama
from colorama import Fore, Back, Style
import wikipedia as wikis
from googlesearch import search
import requests
import json
#import hashlib

colorama.init(autoreset=True)

un = getpass.getuser()
print(f'Welcome ' + Fore.RED + f'{un}!')

#base variables
lis = sr.Recognizer()
tts = pyttsx3.init()
try:
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        description TEXT NOT NULL
    );
    ''')
except Error:
    print(f'An error occurred, error code: {Error.code}')
#functions
def quotation():
    url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    url = url.json()
    dollar = url['USDBRL']['bid']
    eur = url['EURBRL']['bid']
    btc = url['BTCBRL']['bid']
    print(f'USD: {dollar}\nEUR: {eur}\nBTC: {btc}')
    print('This values will be updated on 30s.')
def search_on_google2():
    try:
        search_topic = input("What you want to search?\n >  ")
        url = f'https://www.google.com/search?q={search_topic}'
        webbrowser.open_new_tab(url)
    except KeyboardInterrupt:
        menu()
def search_on_google():
    try:
        search_text = input("What do you want to search?\n >  ")
        pwk.search(search_text)
    except KeyboardInterrupt:
        menu()
def search_related_links_on_google():
    try:
        stext = input('What do you want to search?\n >  ')
        for result in search(f'"{stext}" google', stop=10):
            print(Fore.CYAN + 'Result: ' + Fore.RED + '[' + Fore.GREEN + f'{result}' + Fore.RED +']')
    except KeyboardInterrupt:
        menu()
def play_on_youtube():
    search_video = input("What video you want to play on youtube?\n >  ")
    pwk.playonyt(search_video)
def wiki_verify(info):
    try:
        to_search = wikis.search(str(info))
        for i in to_search:
            print(f'[*]: {wikis.summary(i, sentences=1)}\n')
    except ValueError:
        print("Unknown value. Try again :D")
    except KeyboardInterrupt:
        menu()
'''
def IsAlink(info):
    link1 = 'https://'
    link2 = 'http://'
    if link1 and link2 not in info:
        print(f'{info}: is not a link!')
    else:
        wiki_verify(info)
'''
def speak(text):
    tts.say(text)
    tts.runAndWait()
def speech_recognition():
    try:
        language_choice = input("What language you want?(pt/en)\n >  ")
        if language_choice == "en":
            with sr.Microphone() as mic:
                print("Start to speak...\n")
                while True:
                    print("Press ctrl + c to stop.")
                    audio = lis.listen(mic)
                    sr_text = lis.recognize_google(audio, language="en")
                    with open('text.txt', 'a') as file:
                        file.write(f'{sr_text}\n')
                    print("Saved")
        elif language_choice == "pt":
            with sr.Microphone() as mic:
                print("Começe a falar...\n")
                while True:
                    print("Pressione ctrl + c para encerrar.")
                    audio = lis.listen(mic)
                    sr_text = lis.recognize_google(audio, language="pt")
                    with open('text.txt', 'a') as file:
                        file.write(f'{sr_text}\n')
                    print("Salvo")
        else:
            print(f'{language_choice}: is invalid')
    except ValueError:
        print("Unknown value. Try again :D")
    except KeyboardInterrupt:
        menu()
def counter():
    time_to_sleep = int(input("Time to sleep\n >  "))
    r = 1
    while r <= time_to_sleep:
        print(f'Counter: {r}')
        speak(r)
        r += 1
    speak('Time finished!')
def add_contact_to_db(name, contact, description):
    try:
        cursor.execute(f'''
        INSERT INTO contacts (name, phone, description)
        VALUES ('{name}', '{contact}', '{description}')
        ''')
        conn.commit()
        conn.close()
    except Error:
        print(f'An error occurred, error code: {Error.code}')
    finally:
        conn.close()
def view_contact():
    try:    
        choice_description = input("Want to see contact description?(y/n)\n >  ")
        if choice_description == "y":
            cursor.execute('''
            SELECT * FROM contacts;
            ''')
            for c in cursor.fetchall():
                print(f'Contact info: {c}')
            conn.close()
        elif choice_description == "n":
            cursor.execute('''
            SELECT id, name, phone FROM contacts;
            ''')
            for c in cursor.fetchall():
                print(f'Contact info: {c}')
            conn.close()
        else:
            print(f'{choice_description} is not a valid choice')
            conn.close()
            sleep(10)
            sys.exit()
    except Error:
        print(f'An error occurred, error code: {Error.code}')
    finally:
        conn.close()
def view_contact_open():
    try:
        choice_description = input("Want to see contact description?(y/n)\n >  ")
        if choice_description == "y":
            cursor.execute('''
            SELECT * FROM contacts;
            ''')
            for c in cursor.fetchall():
                print(f'Contact info: {c}')
        elif choice_description == "n":
            cursor.execute('''
            SELECT id, name, phone FROM contacts;
            ''')
            for c in cursor.fetchall():
                print(f'Contact info: {c}')
        else:
            print(f'{choice_description} is not a valid choice')
            conn.close()
            sleep(10)
            sys.exit()
    except Error:
        print(f'An error occurred, error code: {Error.code}')
    finally:
        conn.close()
def remove_contact_to_db():
    try:
        view_contact_open()
        remove_choice = int(input("To remove a contact in the list of contacts you have to enter the contact id\n >  "))
        cursor.execute(f'''
        DELETE FROM contacts
        WHERE id = {remove_choice}
        ''')
        conn.commit()
        conn.close()
    except Error:
        print(f'An error occurred, error code: {Error.code}')
    finally:
        conn.close()
def update_contact_data():
    try:
        view_contact_open()
        contact_id = int(input("Enter the contact id\n >  "))
        new_name = input("Please enter new contact name\n >  ")
        new_phone_number = input("Please enter contact new phone number\n >  ")
        new_description = input("Please enter new contact description\n >  ")
        cursor.execute(f'''
        UPDATE contacts
        SET name = '{new_name}', phone = '{new_phone_number}', description = '{new_description}'
        WHERE id = {contact_id}
        ''')
        conn.commit()
        conn.close()
    except Error:
        print(f'An error occurred, error code: {Error.code}')
    finally:
        conn.close()
def tts_func(content):
    tts.save_to_file(content, 'audio.mp3')
    tts.runAndWait()
def save_tts_audio():
    text = input("Text to transform in audio\n >  ")
    ask_hear_audio = input("Do you want to hear the audio?(y/n)\n >  ")
    if ask_hear_audio == "y":
        speak(text)
        tts_func(text)
    elif ask_hear_audio == "n":
        tts_func(text)
    else:
        print(f'{ask_hear_audio}: is invalid')
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
    search_choice = input("Dou you want to search about this topic before send the message? Can be a fake news.(y/n)\n >  ")
    if search_choice == "y":
        wiki_verify(content)
        ask_send = input("Do you want to send the message(y/n)\n >  ")
        if ask_send == "y":
            pwk.sendwhatmsg(phone_n, content, h, m, wt)
        elif ask_send == "n":
            menu()
        else:
            print(f'{ask_send}: is invalid')
    elif search_choice == "n":
        pwk.sendwhatmsg(phone_n, content, h, m, wt)
    else:
        print(f'{search_choice}: is invalid')
        pwk.sendwhatmsg(phone_n, content, h, m, wt)
def spammer(text, reapeter, delay):
    i = 0
    j = 30
    webbrowser.open_new_tab('web.whatsapp.com')
    print("Choose the contact do you want to spam")
    while i <= j:
        #sleep(1)
        print(f'Counter: {i}')
        speak(i)
        i += 1
    for a in range(reapeter):
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        pyautogui.sleep(delay)
        print(f'You sent {a} messages')
    pyautogui.hotkey("ctrl", "w")
    speak('Finished')
    print('Finish')
def send_msg_for_group():
    group_id = input("Group id\n >  ")
    group_msg = input("Message\n >  ")
    gh = int(input("Hour the message will be sent\n >  "))
    gm = int(input("Minute the message will be sent\n >  "))
    gd = int(input("Delay\n > "))
    pwk.sendwhatmsg_to_group(group_id, group_msg, gh, gm, gd)
def send_random_msg():
    def random_msg():
        msgs = ['Hi', 'Hello', 'Funny', 'Thanks', 'I love you', 'Wtf', 'Jesus christ', 'Fuck', 'Smurfs', 'Potato', 'Tomato', 'Juice', 'Orange', 'Apple', 'Microsoft', 'Linux', 'Is better', 'Shit', '...', ';-;', ':D', ':p', ':3', '<3', "'-'", '=)', '=(']
        random_msg_choice = choice(msgs)
        return random_msg_choice
    user_phone_number = input("User phone number\n >  ")
    msg_hour = int(input("Hour the message will be sent\n >  "))
    msg_min = int(input("Minute the message will be sent\n >  "))
    msg_delay = int(input("Message sent delay\n >  "))
    send_msg(user_phone_number, random_msg(), msg_hour, msg_min, msg_delay)
def send_msg_for_many_contacts():
    contact_list = []
    content_of_msg = input("Message content\n >  ")
    msg_hour1 = int(input("Hour the message will be sent\n >  "))
    msg_min1 = int(input("Minute the message will be sent\n >  "))
    delay1 = int(input("Message sent delay\n > "))
    contact_reapeter = int(input("Number of contacts to send messages\n >  "))
    for s in range(contact_reapeter):
        contact_number_ask = input(f"{s} contact\n >  ")
        contact_list.append(contact_number_ask)
        print(f'{s}: {contact_list}')
    for w in range(contact_reapeter):
        send_msg(contact_list[w], content_of_msg, msg_hour1, msg_min1, delay1)
def send_img():
    msg_contact = input("Number of the contact\n >  ")
    #msg_hour_send = int(input("Hour the message will be sent\n >  "))
    #msg_min_send = int(input("Minute the message will be sent\n >  "))
    img_title = input("Image title\n >  ")
    img_path = input("Image path\n >  ")
    send_delay = int(input("Delay\n >  "))
    pwk.sendwhats_image(msg_contact, img_path, img_title, send_delay)
#inputs and verifications
def menu():
    try:
        escolha_inicial = input("What do you want to do? \n1. Send message \n2. Send random message\n3. Spam\n4. Send encrypted message\n5. Exit\n6. Create contact\n7. View contacts\n8. Counter\n9. Delete contact\n10. Update contact info\n11. Create audio\n12. Send messages for many contacts\n13. Speech recognition\n14. Send image\n15. Send messages for group" + Fore.GREEN + "\n-----------------------------------------------\nSearch functions\n" + Fore.RESET + "16. Search related links on google\n17. Search on google\n18. Search topic on google\n" + Fore.GREEN + "-----------------------------------------------" + Fore.RESET + "\n19. Play video on YouTube\n20. See USD, EUR and BTC quotation" + "\n >  ")

        if escolha_inicial == "5":
            print('Bye Bye :D')
            sleep(5)
            sys.exit()
        elif escolha_inicial == "4":
            cipher_text = input("Your message here\n >  ")
            encrypt(cipher_text)
        #elif escolha_inicial == "1":    
        #    send_msg()
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
        elif escolha_inicial == "6":
            contact_name = input("Contact name\n >  ")
            contact_phone_number = input("Contact phone number\n >  ")
            contact_description = input("Contact short description\n > ")
            add_contact_to_db(contact_name, contact_phone_number, contact_description)
        elif escolha_inicial == "7":
            view_contact()
        elif escolha_inicial == "8":
            counter()
        elif escolha_inicial == "9":
            remove_contact_to_db()
            print("Contact deleted")
        elif escolha_inicial == "10":
            update_contact_data()
        elif escolha_inicial == "11":
            save_tts_audio()
        elif escolha_inicial == "12":
            send_msg_for_many_contacts()
        elif escolha_inicial == "13":
            speech_recognition()
        elif escolha_inicial == "14":
            send_img()
        elif escolha_inicial == "15":
            send_msg_for_group()
        elif escolha_inicial == "16":
            search_related_links_on_google()
        elif escolha_inicial == "19":
            play_on_youtube()
        elif escolha_inicial == "17":
            search_on_google()
        elif escolha_inicial == "18":
            search_on_google2()
        elif escolha_inicial == "20":
            quotation()
        else:
            print(f'{escolha_inicial} is invalid')
    except ValueError:
        print("Unknown value. Try again :)")
        menu()
    except KeyboardInterrupt:
        exit_choice = input("Dou you want to exit?(y/n)\n >  ") 
        if exit_choice == "y":  
            print("Bye Bye :D")
            sleep(10)
            sys.exit()
        elif exit_choice == "n":
            menu()
        else:
            print(f'{exit_choice}: is invalid')
    finally:
        print(Fore.GREEN + "End" + Fore.BLUE +  " of" + Fore.YELLOW + " the" + Fore.RED + " script")
        sleep(5.5)
        sys.exit()
menu()
#Beta version, feel free to contribute
