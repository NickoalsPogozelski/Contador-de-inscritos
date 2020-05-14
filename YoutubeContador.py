import urllib.request
import json
import keyboard
from playsound import playsound
import time

OldSubCount = '0'

def subscribers():
    global OldSubCount

    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id={}&key={}").read() #substitua as chaves pelo id do seu canal e sua key
    subs = (json.loads(data)["items"][0]["statistics"]["subscriberCount"])

    if OldSubCount == '0':
        OldSubCount = subs

    if subs > OldSubCount:       
        playsound('{}') #substitua as chaves pelo caminho para o arquivo de som
        OldSubCount = subs
        
    print(subs)


while True:
    time.sleep(3) #add um delay de 3 segundos
    subscribers()
    
    if keyboard.is_pressed('esc'):
        break
