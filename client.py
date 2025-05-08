import requests
import json
from server import LOCAl_IP
from server import DEFAULT_PORT

URL = f"http://{LOCAl_IP}:{DEFAULT_PORT}/"

def main():
    response = requests.get(URL)
    return(response)


def enviar_mensaje():
    while True:     
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        mensaje = input("Escribe el mensaje a enviar: ")
        json_data = {'mensaje': mensaje} 
        enviar = requests.post(URL, json=json_data, headers=headers)
        print(enviar)  


enviar_mensaje()