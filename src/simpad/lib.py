"""
This script was created entirely by Ashe Muller over the course of literally an entire day.
Please, do credit me if you use this driver. I actually had to do this from the bottom up.
"""

from pywinusb import hid

class SimpadDriver:
    def __init__(self):
        self.device = self.get_device()
        if self.device:
            self.device.open()
            print("Fetched SimPad device successfully.")
        else:
            print("Could not fetch device.")
            
    def get_device(self):
        """ 
        Returns the first device found with the vendor id for simPad (0x8088)
        """
        filter = hid.HidDeviceFilter(vendor_id = 0x8088) # Filter by the SimPad vendor ID
        devices = filter.get_devices()
        if len(devices) > 0: # Make sure there is at least 1 device with the vendor ID
            return devices[0]
        else:
            print("No devices found")
            return False

    def getHexes(self, rgb):
        """
        First is the key (06 for left, 07 for right) followed by the r,g,b values, followed by 0x04 
        (100% brightness), and finished with elements 2-5 to each other's powers consecutively as hex
        """
        if rgb.find("#") != -1:
            rgb = tuple(int(rgb.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        else:
            rgb = tuple(int(rgb[i:i+2], 16) for i in (0, 2, 4))
        arr = [0x07, rgb[0], rgb[1], rgb[2], 0x04, 0x00]
        arr[5] = arr[1] ^ arr[2] ^ arr[3] ^ arr[4]
        return arr
    
    def changeRGB(self, hexcolor, keymode="all"):
        """
        Change the color of both keys to a hex color.
        Usage: SimpadDriver.changeRGB("#FF0000", keymode="all") or SimpadDriver.changeRGB("FF0000", keymode="all")
        Keymode arguments: all | left | right
        """
        match keymode:
            case "left":
                key = [0x06]
            case "right":
                key = [0x07]
            case default:
                key = [0x06,0x07]
        for k in range(len(key)):
            buffer= [0x00]*65
            bufferIn = self.getHexes(hexcolor) ## New in this version: I figured out how to get the rgb lmao
            for y in range(6):
                buffer[y]=bufferIn[y-1]
            ## Change around a few values that fail to get edited usually
            buffer[0]=0x00
            buffer[1]=key[k-1]
            buffer[6]=bufferIn[5]
            out_report = self.device.find_output_reports()
            out_report[0].set_raw_data(buffer)
            out_report[0].send()
    
    def blackout(self):
        """
        Resets color to black (Used when transitioning in between levels and the menu, restarting songs (still not fixed yets), etc.)
        """
        key = [0x06,0x07]
        for k in range(2):
            buffer= [0x00]*65
            bufferIn = [0x06, 0x00, 0x00, 0x00, 0x04, 0x04]
            for y in range(6):
                buffer[y]=bufferIn[y-1]
            ## Change oaround a few values that fail to get edited usually
            buffer[0]=0x00
            buffer[1]=key[k-1]
            buffer[6]=bufferIn[5]
            out_report = self.device.find_output_reports()
            out_report[0].set_raw_data(buffer)
            out_report[0].send()
    
    def off(self):
        """
        Turns simpad lighting off
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x03, 0xFF, 0xFF, 0x04, 0x07]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def on(self):
        """
        Turn simpad lighting to "on"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x02, 0xFF, 0xFF, 0x04, 0x06]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def rainbow(self):
        """
        Turn simpad lighting mode to "rainbow"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x06, 0xFF, 0xFF, 0x04, 0x02]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def fadeout(self):
        """
        Turn simpad lighting mode to "fade out"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x00, 0xFF, 0xFF, 0x04, 0x04]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()

    def keypress(self):
        """
        Turn simpad lighting mode to "key press"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x05, 0xFF, 0xFF, 0x04, 0x01]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def onoff(self):
        """
        Turn simpad lighting mode to On-Off
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x08, 0xFF, 0xFF, 0x04, 0x0C]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def rainbow_fadeout(self):
        """
        Turn simpad lighting mode to "rainbow fadeout"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x07, 0xFF, 0xFF, 0x04, 0x03]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
    
    def rainbow_onoff(self):
        """
        Turn simpad lighting mode to "Rainbow On-Off"
        """
        buffer = [0x00]*65
        bufferIn = [0x08, 0x09, 0xFF, 0xFF, 0x04, 0x0D]
        for y in range(6):
            buffer[y] = bufferIn[y-1]
        buffer[0] = 0x00
        buffer[6] = bufferIn[5]
        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(buffer)
        out_report[0].send()
