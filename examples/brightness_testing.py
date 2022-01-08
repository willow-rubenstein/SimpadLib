from simpadlib import simpad
import time

controller = simpad.Controller()
controller.set_mode(simpad.Mode.on)

for item in ["25%", "50%", "75%", "100%"]:
    controller.set_color(color="#FFFFFF", brightness=item)
    time.sleep(1)