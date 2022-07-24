import audio
import random
import os
import buttons
import display

SOUND_BASE_DIR="/apps/python/soundboard/sounds"

sounds = os.listdir(SOUND_BASE_DIR)
n_sounds = len(os.listdir(SOUND_BASE_DIR))
menuItem = 0

def play_random_sound():
    rand = random.randint(0, n_sounds - 1)
    sound = SOUND_BASE_DIR + "/" +  sounds[rand]
    print(sound)
    channel_id = audio.play(sound, volume=150)

def play_selected_sound():
    sound = SOUND_BASE_DIR + "/" +  sounds[menuItem]
    channel_id = audio.play(sound, volume=150)

def on_action_btn(pressed):
    if pressed:
        #play_random_sound()
        play_selected_sound()

def renderMenu(nextMenuItem):
    global menuItem
    y = 5
    print(display.size())
    # TODO: Scroll if display height is reached (y = 240px)
    display.drawFill(0xFFFFFF)
    for i in range(len(sounds)):
        if i == nextMenuItem:
            display.drawText(10, y, sounds[i], 0xFF0000)
        else:
            display.drawText(10, y, sounds[i], 0x000000)
        y = y + 15
    display.flush()
    menuItem = nextMenuItem

def on_action_btn_up(pressed):
    if pressed:
        if menuItem == 0:
            newMenuItem = n_sounds - 1
        else:
            newMenuItem = menuItem - 1
        renderMenu(newMenuItem)

def on_action_btn_down(pressed):
    if pressed:
        if menuItem == n_sounds:
            newMenuItem = 0
        else:
            newMenuItem = menuItem + 1
        renderMenu(newMenuItem)

renderMenu(0)
buttons.attach(buttons.BTN_A, on_action_btn)
buttons.attach(buttons.BTN_UP, on_action_btn_up)
buttons.attach(buttons.BTN_DOWN, on_action_btn_down)
while True:
    continue
