import requests
import json
import subprocess

# URL de la API de OpenAI
url = "https://api.openai.com/v1/models"

# Carga la API Key
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

# Parámetros de solicitud
payload = {"model": "text-davinci-002"}

# Cabecera de solicitud
headers = {"Content-Type": "application/json",
           "Authorization": "Bearer " + api_key}

# Solicitud a la API de OpenAI
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Verificar el código de estado de la respuesta
if response.status_code == 200:

    # Imprime la respuesta de la API de OpenAI
    print(response.json())

    # Preguntar al usuario si desea ejecutar el programa
    ejecutar = input("¿Desea ejecutar el programa? (s/n): ")

    # Si el usuario elige ejecutar el programa, lo ejecuta
    if ejecutar.lower() == "s":
        comando = input("Ingrese el comando a ejecutar: ")
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado.stdout)

else:
    print("Error al solicitar la API. Código de estado: ", response.status_code)
