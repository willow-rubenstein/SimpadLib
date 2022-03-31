"""
This script was created entirely by Willow Rubenstein over the course of literally an entire day.
Please, do credit me if you use this driver. I actually had to do this from the bottom up.
"""

from pywinusb import hid
import enum


class Keys(enum.Enum):
    left = [0x07]
    right = [0x06]
    both = [0x06, 0x07]

class Mode(enum.Enum):
    off = [0x03, 0x07]
    on = [0x02, 0x06]
    rainbow = [0x06, 0x02]
    fadeout = [0x00, 0x04]
    keypress = [0x05, 0x01]
    on_off = [0x08, 0x0C]
    rainbow_fade = [0x07, 0x03]
    rainbow_on_off = [0x09, 0x0D]

## New to 2.0.1 - Added brightness dict
Brightness = {
    "25%": 0x01,
    "50%": 0x02,
    "75%": 0x03,
} 

class Controller:
    def __init__(self):
        self.device = self.__get_device()
        if self.device:
            self.device.open()
            self.device.reporter = self.device.find_output_reports()[0]
            print("Found a device successfully.")
        else:
            print("No devices found")

    def __get_device(self):
        """ 
        Returns the first device found with the vendor id (0x8088) for SimPad 
        """
        filter = hid.HidDeviceFilter(
            vendor_id=0x8088)  # Filter by the SimPad vendor ID
        devices = filter.get_devices()
        if len(devices) > 0:  # Make sure there is at least 1 device with the vendor ID
            return devices[0]
        else:
            return False # Return false if no device is found

    def __parse_color(self, hex_color, brightness):
        """
        First is the key (06 for left, 07 for right) followed by the r,g,b values, 
        hex for brightness (defaults to 0x04, or 100%), and finished with elements 2-5 to each other's powers 
        consecutively as hex. This function should not be used on its own. Users should use set_color instead.

        New in 2.0.1: 
          - Added brightness arg to parse_color (could not add to set_color because of weird syntax errors)
          - Small optimization with removing the # from the hex color string.
        """
        bright = 0x04
        if brightness and brightness in list(Brightness.keys()):
            bright = Brightness[brightness]
        if hex_color.find("#") != -1:
            hex_color = hex_color.replace("#", "")
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        arr = [0x07, rgb[0], rgb[1], rgb[2], bright, 0x00]
        arr[5] = arr[1] ^ arr[2] ^ arr[3] ^ arr[4]
        return arr

    def __send_data(self, data: list):
        """
        Sends the data to the device.
        """
        self.device.reporter.set_raw_data(data)
        self.device.reporter.send()

    def set_color(self, color, keys: Keys = Keys.both, brightness=None):
        """
        Change the color of both keys to a hex color.
        Usage: controller.set_color("#FF0000", keys=Keys.both, brightness=None) or controller.set_color("FF0000", keys=Keys.both, brightness="25%")
        New in 2.0.1: 
          - Changed hex_color to just color.
          - Added brightness argument: Possible values (type: string) are 25%, 50%, 75%, or empty for 100%
        """
        parsed_color_buffer = self.__parse_color(color, brightness)
        buffer = [0x00]*65
        for y in range(6):
            buffer[y+1] = parsed_color_buffer[y]
        for k in range(len(keys.value)):
            buffer[1] = keys.value[k-1]
            self.__send_data(buffer)

    def reset(self):
        """
        Resets the device without turning the device off.
        """
        buffer = [0x00]*65
        buffer[2] = buffer[3] = buffer[4] = 0x00
        buffer[5] = buffer[6] = 0x04

        for k in range(2):
            buffer[1] = Keys.both.value[k]
            self.__send_data(buffer)

    def set_mode(self, mode: Mode):
        """
        Sets the current mode of the device to the mode specified
        Usage: controller.set_mode(<mode>)
        """
        buffer = [0x00]*65
        buffer[1] = 0x08
        buffer[2] = mode.value[0]
        buffer[3] = buffer[4] = 0xFF
        buffer[5] = 0x04
        buffer[6] = mode.value[1]
        self.__send_data(buffer)
