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
soundlists = [sounds[i:i + 13] for i in range(0, len(sounds), 13)]
pages = len(soundlists)

def play_random_sound():
    rand = random.randint(0, n_sounds - 1)
    sound = SOUND_BASE_DIR + "/" +  sounds[rand]
    print(sound)
    channel_id = audio.play(sound, volume=150)

def play_selected_sound():
    print(sounds[sounditem])
    sound = SOUND_BASE_DIR + "/" +  sounds[sounditem]
    channel_id = audio.play(sound, volume=150)

def on_action_btn(pressed):
    if pressed:
        #play_random_sound()
        play_selected_sound()

def renderMenu(nextMenuItem, nextpage):
    global sounditem
    global menuItem
    global page
    y = 5
    # Background (white)
    display.drawFill(0xFFFFFF)

    display.drawText(135, 220, "<", 0x000000)
    x = 150
    for j in range(pages):
        if j == nextpage:
            display.drawText(x, 220, str(j+1), 0xFF0000)
        else:
            display.drawText(x, 220, str(j+1), 0x000000)
        x = x + 15
    display.drawText(x, 220, ">", 0x000000)
    page = nextpage

    for i in range(len(soundlists[page])):
        if i == nextMenuItem:
            display.drawText(10, y, soundlists[page][i], 0xFF0000)
            # Netter maken voor als we meer dan 2 pagina's hebben
            if page != 0:
                sounditem = i + 1 + len(soundlists[page]) + 1
                print(sounds[sounditem])
            else:
                sounditem = nextMenuItem
                print(sounds[sounditem])
        else:
            display.drawText(10, y, soundlists[page][i], 0x000000)
        y = y + 15
    display.flush()
    menuItem = nextMenuItem
  
def on_action_btn_up(pressed):
    # TODO max 13 sounds per page
    if pressed:
        if menuItem == 0:
            newMenuItem = len(soundlists[page]) - 1
        else:
            newMenuItem = menuItem - 1
        renderMenu(newMenuItem, page)

def on_action_btn_down(pressed):
    # TODO max 13 sounds per page
    if pressed:
        if menuItem == len(soundlists[page]):
            newMenuItem = 0
        else:
            newMenuItem = menuItem + 1
        renderMenu(newMenuItem, page)

def on_action_btn_left(pressed):
    if pressed:
        newMenuItem = 0
        if page == 0:
            print("Left")
            newpage = pages - 1
        else:
            newpage = page - 1
        renderMenu(newMenuItem, newpage)

def on_action_btn_right(pressed):
    if pressed:
        newMenuItem = 0
        if page == pages:
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
