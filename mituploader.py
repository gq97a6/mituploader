import requests
import os
import sys

#Get current working dir
dir = os.path.dirname(sys.executable)

#Check if users.txt exists
if not os.path.isfile(dir + "\\users.txt"):
    print("No users.txt found in current directory. Exiting...")
    sys.exit()

#Get list of users
users = {}
with open(dir + "\\users.txt", 'r') as f:
    for line in f:
        parts = line.strip().split(':')
        users[parts[0]] = parts[1].split('-')

#Check if users.txt is empty
if len(users) == 0: 
    print("No users found. Exiting...")
    sys.exit()

#Get list of files
filePaths = []
for path in os.listdir(dir):
    if path.endswith(".aia"):
        filePaths.append(path)

#Check if project files exist
if len(filePaths) == 0: 
    print("No files to upload found. Exiting...")
    sys.exit()

#Send each file to each user
for user, blocks in users.items():
    for filePath in filePaths:
        session = requests.Session()
        response = session.post(
            "https://code.appinventor.mit.edu/login",
            data = {
                "A": blocks[0],
                "B": blocks[1],
                "C": blocks[2],
                "D": blocks[3],
                "locale": "en",
                "revisit": "true",
                "host": "code.appinventor.mit.edu"
        })

        if response.status_code != 200:
            print("Failed to login as " + user)
            session.close()
            break

        with open(dir + "//" + filePath, 'rb') as file:
            payload = {'uploadProjectArchive': ('file.bin', file, 'application/octet-stream')}
            url = 'https://code.appinventor.mit.edu/ode/upload/project/' + filePath[:-4]
            response = session.post(url, files = payload)

            if response.status_code != 200:
                print("Failed to upload " + filePath + " to " + user)
                session.close()
                break

        session.close()
        print("Send " + filePath + " to " + user)