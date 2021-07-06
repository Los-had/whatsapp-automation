# whatsapp-automation
 Automating whatsapp with python
# used on this project
- [x] pyautogui
- [x] pywhatkit
- [x] pyttsx3
- [x] SpeechRecognition
    * embedded in python
        - [x] time
        - [x] random
        - [x] sys
        - [x] webbrowser
        - [x] sqlite3 and sqlite3 Error
    
# why?
I created this project to improve myself and study a little more in the subjects of python and task automation

# using
***WARNING: this program needs sqlite3 db installed to work properly.***

***WARNING: this program needs internet connection to work properly.***

download the dependencies running this commands on your terminal 
```
cd ./whatsapp-automation
cd ./app
cd ./dependencies
pip install -r requirements.txt
``` 
or the executing the file ``denpendencies.cmd`` or ``dependencies.sh`` when the installing processes finish 
download the project in the github after that open your terminal and write 
```
cd ./whatsapp-automation
cd ./app
python app.py
```

# mvp

- [x] send messages 
    - [x] send encrypted messages  | [features](#sem)
    - [x] send random messages | [features](#srm)
- [x] embedded spammer | [features](#spammerfeatures)

## Extra features
- [x] Contacts sqlite db | [features](#cdbf)
    - [x] view all the contacts in the list,
    - [x] add contacts in the list,
    - [x] delete contacts in the list
    - [x] update contact info
- [ ] send other types of media on whatsapp like videos, photos and more.

# Features

<div id="spammerfeatures">
    <h3>embedded spammer features</h3>
    <ul>
        <li>embedded time counter, with voice</li>
        <li>custom messages delay</li>
        <li>custom messages content</li>
        <li>uses pyautogui for more faster spam</li>
    </ul>
</div>
<div id="sem">
    <h3>encrypted message features</h3>
    <ul>
        <li>embedded Caesar cipher encryption system, with voice</li>
        <li>custom messages delay</li>
        <li>custom messages content</li>
        <li>custom cipher key</li>
    </ul>
</div>
<div id="srm">
    <h3>random message features</h3>
    <ul>
        <li>embedded random message function</li>
        <li>custom messages delay</li>
    </ul>
</div>
<div id="cdbf">
    <h3>Contacts.db crud</h3>
    <ul>
        <li><i>C</i>reate contacts</li>
        <li><i>R</i>ead contacts</li>
        <li><i>U</i>pdate contacts</li>
        <li><i>D</i>elete contacts</li>
    </ul>
</div>
