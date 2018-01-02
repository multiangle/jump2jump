__author__ = 'multiangle'

import os, sys
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

def action(t):
    q = '{} shell input swipe 500 500 510 520 {}'.format(adb_path, t)
    print(q)
    os.system(q)

if __name__=='__main__':
    dist = sys.argv[1]
    dist = float(dist)
    duration = round(dist*100*2.6)
    print(duration)
    action(duration)



# print(os.path.abspath('.'))
# print(x)