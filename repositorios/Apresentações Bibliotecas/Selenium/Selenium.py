import pyautogui
import time

# Pausa entre comandos para o sistema responder
pyautogui.PAUSE = 0.05

# Abrir o menu iniciar
pyautogui.press('win')
time.sleep(0.3)

# Digitar "Firefox"
pyautogui.write('firefox', interval=0.02)
time.sleep(0.7)

# Pressionar Enter para abrir o Firefox
pyautogui.press('enter')

# Esperar o Firefox abrir
time.sleep(0.7)

# Digitar a URL do WhatsApp Web
pyautogui.write('https://google.com', interval=0.03)
pyautogui.press('enter')

time.sleep(1.3)

pyautogui.press('enter')
pyautogui.write('Gabriel Pato', inverval=0.07)
pyautogui.press('enter')