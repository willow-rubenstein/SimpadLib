# SimpadLib v2.1

### Example Usages
```py
from simpad.lib import simpad

sim = simpad.Controller() # Initialize the SimPad class
sim.changeRGB("#FF000", keys=simpad.Keys.Both) # Change all keys to color "#FF0000"
sim.changeRGB("#00FF00", keys=simpad.keys.Left) # Change the left key's color to "#00FF00"
```

```py
from simpad.lib import simpad

sim = simpad.Controller() # Initialize the SimPad class
sim.changeRGB("#FF000", keys=simpad.Keys.Both, brightness="25%") # Change all keys to color "#FF0000", but only with 25% brightness
sim.changeRGB("#00FF00", keys=simpad.keys.Left, brightness="50%") # Change the left key's color to "#00FF00", but only with 50% brightness
```