__author__ = 'multiangle'

import os
import matplotlib.image as img
import matplotlib.pyplot as plt

adb_path = 'D:\\multiangle\\software_Add\\AndroidStudio\\SDK\\platform-tools\\adb.exe '
if not os.path.exists('pic'):
    os.mkdir('pic')

def getScreen(id=1):
    q = adb_path + 'shell screencap -p /sdcard/1.png'
    os.system(q)
    q = adb_path + 'pull /sdcard/1.png pic/{}.png'.format(id)
    os.system(q)
    q = adb_path + 'shell rm /sdcard/1.png'
    os.system(q)

def matchImage():
    pass

getScreen(2)

# print(os.path.abspath('.'))
# print(x)