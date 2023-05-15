import os

if __name__ == '__main__':
    print("Welcome to Robo speaker 0.1 created by Firoz")
    while True:
        word = input("Enter what you want to pronounce:")
        if word == "q":
            break
        command = f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{word}');"
        os.system(command)
