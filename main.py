__author__ = 'multiangle'

import os, sys
import numpy as np
import PIL
import PIL.Image as Image
import matplotlib.pyplot as plt
from pprint import pprint

adb_path = 'D:\\multiangle\\software_Add\\AndroidStudio\\SDK\\platform-tools\\adb.exe '  # for my notebook
# adb_path = 'E:\\multiangle\\software\\AndroidStudio\\SDK\\platform-tools\\adb.exe '                 # for my PC

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

def imgaeMatch(file_name='1.png'):
    def comparePix(pattern_np, part_np):
        assert np.shape(pattern_np)==np.shape(part_np)
        # value = 0
        # [s1, s2, s3] = np.shape(pattern_np)
        diff = pattern_np[:,:,:3] - part_np[:,:,:3]
        diff_abs = np.abs(diff)
        diff_2d = np.sum(diff_abs, axis=2)
        diff_alpha = np.multiply(diff_2d, pattern_np[:,:,3])
        diff_alpha = diff_alpha / 255
        diff_value = np.sum(diff_alpha)
        return diff_alpha, diff_value

    pattern = Image.open('pic\\item.png')
    pattern_np = np.array(pattern, dtype=np.uint8).astype(np.int32)

    ori_img = Image.open(os.path.join('pic', file_name))
    ori_img_np = np.array(ori_img, dtype=np.uint8).astype(np.int32)

    [pt_s1, pt_s2, _] = np.shape(pattern_np)
    [ori_s1, ori_s2, _] = np.shape(ori_img_np)

    min_value = 100000000
    min_index = -1

    for i in range(0, ori_s1-pt_s1,5):
        for j in range(0,  ori_s2-pt_s2,5):
            p_alpha, diff_value = comparePix(pattern_np, ori_img_np[i:i+pt_s1, j:j+pt_s2, :])
            if diff_value<min_value:
                min_index = [i,j]
                min_value = diff_value

    comparePix(pattern_np, ori_img_np[0:210, 0:82, :])
    pprint(pattern_np[:,:,3])
    print(np.shape(pattern_np))
    # plt.imshow(pattern_np[:,:,3])
    # plt.show()
    # print(ori_img[:,:,0])
    # ori_img.show()
    # print(np.shape(pattern))

if __name__=='__main__':
    # dist = sys.argv[1]
    # dist = float(dist)
    # duration = round(dist*100*2.6)
    # print(duration)
    # action(duration)

    imgaeMatch('2.png')


# print(os.path.abspath('.'))
# print(x)