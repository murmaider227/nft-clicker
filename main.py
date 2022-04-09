import time

import pyautogui

#pyautogui.MINIMUM_DURATION = 0.5


flower_list = ['flower4']
chest_list = ['chest4']
collected_flowers = []
previous_flower=None


def find_object(img, confidence=0.99):
    coordinates = pyautogui.locateOnScreen(f'img/{img}.png', confidence=confidence)
    return coordinates


def find_chest():
    for item in chest_list:
        chest = find_object(item, confidence=0.8)
        if chest is not None:
            pyautogui.moveTo(chest)
            pyautogui.click()
            print('found chest')
            time.sleep(0.5)
        close_chest = find_object('close_chest', confidence=0.8)
        if close_chest is not None:
            print("closed chest")
            pyautogui.click(close_chest)
            return close_chest
        return chest


while 1:
    for item in flower_list:
        flower = find_object(item)
        if flower is not None:
            pyautogui.moveTo(flower)
            pyautogui.move(0, 20)
            coordinates = pyautogui.position()
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.click()
            if find_chest() is not None:
                time.sleep(1)
                pyautogui.click(coordinates)
                if previous_flower is not None:
                    pyautogui.moveTo(previous_flower)
                    pyautogui.click()
                    #print('clicked previous')
                    pyautogui.move(0, 40)
            previous_flower=flower


