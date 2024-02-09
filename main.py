import pyautogui
import time

letters = ['a','b','c','d']

numbers = [1,2,3,4]

pyautogui.alert("The code will start")
time.sleep(2)
posicao = pyautogui.position()
print(posicao)

for i in range(len(letters)):

    # Field nome
    pyautogui.click(x=761, y=364)
    time.sleep(1)

    # Entering Letters
    pyautogui.write(letters[i])

    # Field Numbers
    pyautogui.press('tab')
    time.sleep(1)

    # Entering Numbers
    pyautogui.write(numbers[i])

    if i == len(letters) - 1:
        break

pyautogui.alert("Finished Code")
