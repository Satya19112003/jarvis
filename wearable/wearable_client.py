import requests

SERVER = "http://localhost:5000/command"

def send_command(cmd):
    response = requests.post(SERVER, json={"cmd": cmd})
    print(response.json())

send_command("heart rate check")

