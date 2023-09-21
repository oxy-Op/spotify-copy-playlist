import pyautogui
import keyboard
from time import sleep


def find_identifier():
    try:
        x = pyautogui.center(pyautogui.locateOnScreen("time2.png"))
        pyautogui.moveTo(x[0], x[1] + 60)
    except TypeError:
        raise TypeError("Could not locate identifier")


def find_dots():
    try:
        x = pyautogui.center(pyautogui.locateOnScreen("three_dots.png"))
        return x[0], x[1]
    except TypeError:
        raise TypeError("Could not locate three dots")


def click_dots():
    try:
        pyautogui.click(find_dots())
    except Exception as e:
        print("Could not click dots, exiting...")
        # exit()


def add_to_playlist():
    try:
        x = pyautogui.center(pyautogui.locateOnScreen("add.png", confidence=0.9))
        pyautogui.moveTo(x[0], x[1])
    except TypeError:
        raise TypeError("Could not locate `add to playlist`")


def find_playlist():
    try:
        screen_width, screen_height = pyautogui.size()
        search_region = (screen_width // 2, 0, screen_width // 2, screen_height)
        x = pyautogui.center(
            pyautogui.locateOnScreen("playlist.png", region=search_region)
        )
        pyautogui.click(x[0], x[1])
    except TypeError:
        raise TypeError("Could not locate playlist")


def key(k):
    if k.name == "f4":
        print("Key Pressed")
        find_identifier()
    while 1:
        sleep(1)
        click_dots()
        add_to_playlist()
        find_playlist()
        pyautogui.scroll(-8)
        sleep(0.5)
        pyautogui.moveTo(100, 200)
        pyautogui.press("down")


keyboard.on_press(key)

while True:
    keyboard.wait("f2")
    break
