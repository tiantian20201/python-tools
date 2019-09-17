import cv2 as cv
import numpy as np
import os


# 属性读取,修改位数据
def change_color(image, newfile):
    # print(image.shape)
    heigh = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    # print("heigth: %s, width: %s, channels: %s" % (heigh, width, channels))
    for row in range(heigh):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imwrite(newfile, image)


def GetFileList(dir, fileList, notdeal=[]):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            if s in notdeal:
                continue
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList, notdeal)
    return fileList


# 修改一半的图像数据
filepath_test = "./datasets/test_examples_labels/test_new"
lists_test = GetFileList(filepath_test, [])
for i in range(len(lists_test)):
    if (i % 2 == 1):
        print(i)
        # src = cv.imread(lists_test[i])  # 加载图片资源
        # change_color(src,lists_test[i])
    i += 1

filepath_train = "./datasets/train_examples_labels/train_new"
lists_train = GetFileList(filepath_train, [])
for i in range(len(lists_train)):
    if (i % 2 == 1):
        print(i)
        # src = cv.imread(lists_train[i])  # 加载图片资源
        # change_color(src,lists_train[i])
    i += 1
