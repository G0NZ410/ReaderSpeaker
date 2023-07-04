import time
import pyperclip
import pyttsx3

def subrayar_texto():
    time.sleep(2)
    texto_copiado = pyperclip.paste()
    return texto_copiado

toSpeak = pyttsx3.init()
toSpeak.setProperty('rate', 125)
toSpeak.say(subrayar_texto())
toSpeak.runAndWait()
