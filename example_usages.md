# SimpadLib v2.2

### Example Usages
```py
from simpadlib import simpad

sim = simpad.Controller() # Initialize the SimPad class
sim.changeRGB("#FF000", keys=simpad.Keys.both) # Change all keys to color "#FF0000"
sim.changeRGB("#00FF00", keys=simpad.keys.left) # Change the left key's color to "#00FF00"
```

```py
from simpadlib import simpad

sim = simpad.Controller() # Initialize the SimPad class
sim.changeRGB("#FF000", keys=simpad.Keys.both, brightness="25%") # Change all keys to color "#FF0000", but only with 25% brightness
sim.changeRGB("#00FF00", keys=simpad.keys.left, brightness="50%") # Change the left key's color to "#00FF00", but only with 50% brightness
```