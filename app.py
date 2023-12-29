import pyautogui
from time import sleep

#Utilizar o mouseInfo()
#Comando 1 from mouseinfo import mouseInfo
#Comando 2 mouseInfo()

# Descrição do Processo:

# 1. Abrir navegador
pyautogui.click(645,1048,duration=2)
pyautogui.click(227,61,duration=2)
# 2. digitar o link do sistema
pyautogui.write('http://187.9.102.123:9095')
pyautogui.press('enter')
# 3. digitar usuario
sleep(8)

pyautogui.write('ORION402040')
# 4. digitar senha
sleep(1)
pyautogui.press('tab')
pyautogui.write('asd@123')
sleep(1)
# 5. clicar em entrar
pyautogui.click(1076,777,duration=2)
# 6. clicar trocar de modulo
sleep(5)
pyautogui.click(837,647,duration=2)
sleep(5)
pyautogui.write('09')
# 8. clicar em entrar
pyautogui.click(1058,801,duration=2)
sleep(5)
# 9. criar no menu miscelanea
pyautogui.click(630,1057,duration=3)
sleep(2)
pyautogui.click(101,622,duration=3)
sleep(2)
pyautogui.click(108,703,duration=3)
sleep(2)
pyautogui.click(114,778,duration=3)
sleep(2)
pyautogui.click(1061,756,duration=3)
sleep(10)
pyautogui.click(64,433,duration=3)
pyautogui.click(437,433,duration=3)
pyautogui.click(1861,995,duration=3)


# 10. Extrator
