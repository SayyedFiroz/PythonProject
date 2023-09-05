import requests
import json
import os


city = input("Enter the city name\n")

url = f"http://api.weatherapi.com/v1/current.json?key=334fe93717154f6baf1173220232905&q={city}"
req = requests.get(url)

wdic = json.loads(req.text)
voice_temp =wdic["current"]["temp_c"]
print(voice_temp)


command = f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{city}{voice_temp}');"
os.system(command)
