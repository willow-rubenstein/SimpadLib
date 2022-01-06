# SimpadLib

### Example Usages
```py
from simpad.lib import SimPad

sim = SimPad() # Initialize the SimPad class
sim.changeRGB("#FF000", "all") # Change all keys to color "#FF0000"
sim.blackout() # Reset the color palette/black out keys (turns keys off)
```

```py
from simpad.lib import SimPad

sim = SimPad()
sim.rainbow() # Turn rainbow mode on
sim.off() # Turn simpad off (does not change state)
sim.on() # Turns simpad on with specified original colors, not with last state
sim.changeRGB("#FF0000")
```
