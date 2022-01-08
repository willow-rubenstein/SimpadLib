from setuptools import setup, find_packages
from pathlib import Path

## I'm just going to manually do this for now.
## I don't think there is an easy way to fix the bug with readme files.
description = """\
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
"""


setup(
    name='simpadlib',
    author='Ashe Muller',
    author_email='contact.notashe@gmail.com',
    version='2.0.1',
    description='A library that allows users to interface with their SimPad devices in real-time',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/malevtuber/simpadlib',
    packages=find_packages(),
    ignore_packages=['examples'],
    python_requires='>=3.10',
    install_requires=['pywinusb>=0.4.2'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/malevtuber/simpadlib/issues'
    }
)
