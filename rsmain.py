import time
import pyperclip
import pyttsx3

def subrayar_texto():
    texto_copiado = pyperclip.paste()
    return texto_copiado

toSpeak = pyttsx3.init()
toSpeak.setProperty('rate', 125)
toSpeak.say(subrayar_texto())
toSpeak.runAndWait()
