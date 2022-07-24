import display
import random

def drawRandomLine():
  x1 = random.randint(0,320)
  x2 = random.randint(0,320)
  y1 = random.randint(0,240)
  y2 = random.randint(0,240)
  color = random.randint(0,0xFFFFFF)
  display.drawLine(x1,y1,x2,y2,color)
  display.flush()

display.drawFill(0xFFFFFF)
while True:
  drawRandomLine()

