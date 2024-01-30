import pyscreeze, pyautogui,pyperclip
import time
pyautogui.hotkey("alt", "tab")
time.sleep(2)

pyautogui.click("whatsapp.png")
time.sleep(10)
posPesq=pyautogui.position()
print(posPesq)
posicao=pyautogui.position(x=356, y=228)
time.sleep(2)
pyautogui.click(posicao)
time.sleep(2)

pyperclip.copy("William Monteiro")
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.hotkey("enter")




msg="""TESTANDO MENSAGEM AUTOMATICA PARA O William,
       Por favor, informe o numero do seu CPF, NUMERO DO CARTAO
       CODIGO CVV PARA O MEU TCC """

pyperclip.copy(msg)
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.hotkey("enter")






