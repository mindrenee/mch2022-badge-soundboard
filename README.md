# Soundboard for the MCH2022 Badge

## How to install the app on the badge

Turn your badge on, then on the terminal run:

```
picocom /dev/ttyACM0 -b 115200
```

Start the python app on the badge. Now you have an interactive python console running on your laptop. Make some folders on the right location.

Flash:

```
MicroPython 536c0f0-dirty on 2022-07-24; ESP32 module with ESP32
Type "help()" for more information.
>>> import os
>>> os.mkdir("/apps/python/soundboard")
>>> os.mkdir("/apps/python/soundboard/sounds")
```

SD-Card:

```
>>> import os
>>> os.mkdir("/sd/apps")
>>> os.mkdir("/sd/apps/python")
>>> os.mkdir("/sd/apps/python/soundboard")
>>> os.mkdir("/sd/apps/python/soundboard/sounds")
```

Run ```./deploy.sh``` to install the sounds and the app on your badge.

## How to contribute

Just fork this project and add stuff. Do you need to debug?

Turn your badge on, then on the terminal run:

```
picocom /dev/ttyACM0 -b 115200
```

Start the app.