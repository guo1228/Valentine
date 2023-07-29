import cv2 as cv
import os

files = os.listdir('./all')
os.makedirs('./save')
for name in files:
    folder_path = './all/' + name
    save_path = './save/' + name
    os.makedirs(save_path)
    pics = os.listdir(folder_path)
    for pic in pics:
        pic_path = folder_path + '/' + pic
        save = save_path + '/' + pic
        img = cv.imread(pic_path)
        factor = img.shape[1]/700
        height = int(img.shape[0]/factor)
        img_after = cv.resize(img, [700, height])
        cv.imwrite(save, img_after)
