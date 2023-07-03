import time
import pyperclip
import pyttsx3

toSpeak = pyttsx3.init()

def subrayar_texto():
    time.sleep(2)
    texto_copiado = pyperclip.paste()
    return texto_copiado

toSpeak.say(subrayar_texto())
toSpeak.runAndWait()
