import cv2 as cv
import os

files = os.listdir('./')
for pic in files:
    if pic[-3:] == 'jpg':
        pic_path = './' + pic
        print(pic)
        save = './' + pic
        img = cv.imread(pic_path)
        factor = img.shape[1]/700
        height = int(img.shape[0]/factor)
        img_after = cv.resize(img, [700, height])
        cv.imwrite(save, img_after)
