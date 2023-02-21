import requests
import os
import sys

#Get current working dir
dir = os.path.dirname(sys.executable)

#Get list of users
users = {}
with open(dir + "\\users.txt", 'r') as f:
    for line in f:
        parts = line.strip().split(':')
        users[parts[0]] = parts[1].split('-')

#Get list of files
files = []
for file in os.listdir(dir):
    if file.endswith(".aia"):
        files.append(file)

#Send each file to each user
for user, blocks in users.items():
    for file in files:
        session = requests.Session()
        session.post(
            "http://code.appinventor.mit.edu/login", 
            data = {
                "A": blocks[0],
                "B": blocks[1],
                "C": blocks[2],
                "D": blocks[3],
                "locale": "en",
                "revisit": "true",
                "host": "code.appinventor.mit.edu"
        })

        with open(dir + "//" + file, 'rb') as f:
            payload = {'uploadProjectArchive': ('file.aia', f)}
            url = 'http://code.appinventor.mit.edu/ode/upload/project/' + file[:-4]
            session.post(url, data = {'host': 'code.appinventor.mit.edu'}, files = payload)
        
        session.close()
    print("Send to " + user)