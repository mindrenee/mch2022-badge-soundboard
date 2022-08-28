from time import sleep
import audio
import random
import os
import buttons
import display
import mch22

SOUND_BASE_DIR="/sd/apps/python/soundboard/sounds"

sounds = os.listdir(SOUND_BASE_DIR)
n_sounds = len(os.listdir(SOUND_BASE_DIR))
menuItem = 0
page = 0
sounditem = 0
soundlists = [sounds[i:i + 10] for i in range(0, len(sounds), 10)]
pages = len(soundlists)
sound = ""

def play_selected_sound():
    global sound
    sound = SOUND_BASE_DIR + "/" + sound
    channel_id = audio.play(sound, volume=150)

def on_action_btn(pressed):
    if pressed:
        play_selected_sound()

# TODO: Make splashscreen 
def spashScreen():
    display.drawFill(0xFFFFFF)

    display.flush()
    sleep(3)

def renderMenu(nextMenuItem, nextpage):
    global sounditem
    global menuItem
    global page
    global sound
    y = 10
    # Background (white)
    display.drawFill(0xFFFFFF)

    display.drawText(135, 220, "<", 0x000000, "ocra16")
    x = 150
    for j in range(pages):
        if j == nextpage:
            display.drawText(x, 220, str(j+1), 0xFF0000, "ocra16")
        else:
            display.drawText(x, 220, str(j+1), 0x000000, "ocra16")
        x = x + 15
    display.drawText(x, 220, ">", 0x000000, "ocra16")
    page = nextpage

    for i in range(len(soundlists[page])):
        if i == nextMenuItem:
            display.drawText(10, y, soundlists[page][i].replace(".mp3", ""), 0xFF0000, "ocra16")
            if page != 0:
                counter = page
                while counter != 0:
                    sounditem = sounditem + len(soundlists[counter-1])
                    counter = counter - 1
                sounditem = sounditem + i 
                sound = sounds[sounditem]
            else:
                sounditem = nextMenuItem
                sound = sounds[sounditem]
        else:
            display.drawText(10, y, soundlists[page][i].replace(".mp3", ""), 0x000000, "ocra16")
        y = y + 18
    display.flush()
    menuItem = nextMenuItem
  
def on_action_btn_up(pressed):
    global sounditem 
    sounditem = 0
    if pressed:
        if menuItem == 0:
            newMenuItem = len(soundlists[page]) - 1
        else:
            newMenuItem = menuItem - 1
        renderMenu(newMenuItem, page)

def on_action_btn_down(pressed):
    global sounditem 
    sounditem = 0
    if pressed:
        if menuItem == len(soundlists[page]) - 1:
            newMenuItem = 0
        else:
            newMenuItem = menuItem + 1
        renderMenu(newMenuItem, page)

def on_action_btn_left(pressed):
    global sounditem 
    sounditem = 0
    if pressed:
        newMenuItem = 0
        if page == 0:
            print("Left")
            newpage = pages - 1
        else:
            newpage = page - 1
        renderMenu(newMenuItem, newpage)

def on_action_btn_right(pressed):
    global sounditem 
    sounditem = 0
    if pressed:
        newMenuItem = 0
        if page == pages - 1:
            newpage = 0
        else:
            newpage = page + 1
        renderMenu(newMenuItem, newpage)

def reboot(pressed):
  if pressed:
    print("Test")
    mch22.exit_python()

buttons.attach(buttons.BTN_HOME,reboot)

renderMenu(0, 0)
buttons.attach(buttons.BTN_A, on_action_btn)
buttons.attach(buttons.BTN_UP, on_action_btn_up)
buttons.attach(buttons.BTN_DOWN, on_action_btn_down)
buttons.attach(buttons.BTN_LEFT, on_action_btn_left)
buttons.attach(buttons.BTN_RIGHT, on_action_btn_right)
while True:
    continue
