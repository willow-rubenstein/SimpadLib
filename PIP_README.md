# SimpadLib v1.1

### Example Usages
```py
from simpad.lib import SimPad

sim = SimPad() # Initialize the SimPad class
sim.changeRGB("#FF000", "all") # Change all keys to color "#FF0000"
sim.changeRGB("#00FF00", "left") # Change the left key's color to "#00FF00"
```

```py
from simpad.lib import SimPad

sim = SimPad()
sim.changeMode("rainbow") # Change mode to rainbow
sim.changeMode("on-off") # Change mode to on-off
sim.changeMode("off") # Turns lights off completely. If you are clearing colors, use sim.clear() instead.
```
