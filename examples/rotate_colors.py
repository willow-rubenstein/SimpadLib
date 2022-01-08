import sys
sys.path.append("..")

import time
from simpadlib import simpad

controller = simpad.Controller()
controller.set_mode(simpad.Mode.on)

for color in ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF"]:
	controller.set_color(color, simpad.Keys.left)
	time.sleep(1)
	controller.set_color(color, simpad.Keys.right)
	time.sleep(1)

controller.reset()