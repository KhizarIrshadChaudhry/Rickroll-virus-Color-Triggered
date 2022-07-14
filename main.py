import pyautogui
from playsound import playsound
from pynput.keyboard import Key, Controller

keyboard = Controller()


def main():
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    playsound("rickAstley.wav")


while True:
    try:
        while True:

            if pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)[0] > 130 and \
                    pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)[1] > 130 and \
                    pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)[2] < 60:
                main()
    except:
        pass
