import cv2
import sys


# todo image:
# r - red       (0 - 255)
# g - green     (0 - 255)
# b - blue      (0 - 255)
# a - alpha     (0 - 100)

# crop - обрезка (пиксели уменьшаются)
# 1.
# ... matrix RGB -> manipulate
#

# resize - изменение размера полотна, само изображение сохраняется (пиксели уменьшаются)

# change quality - изменение качества (пиксели не уменьшаются)

# reverse

# change color to black and white (grayscale)

# find face

# add another image or figure

# todo video
# find face(s)

# data1 = [
# [1, 2, 3],
# [1, 2, 3],
# [1, 2, 3],
# [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print(data1)
# print(data1[:len(data1)//2])

def read_and_show_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"))
    cv2.imshow("Display window", img)
    cv2.waitKey(0)


def crop_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"))
    height, width, channels = img.shape  # (1920, 1080, 3)
    cv2.imshow("Display window", img)
    cv2.imshow("Display window cropped", img[0:height // 2, 0:width // 2])  # y1:y2, x1:x2
    cv2.imshow("Display window cropped2", img[height // 2:height, width // 2:width])  # y1:y2, x1:x2
    cv2.waitKey(0)


def change_to_gray_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"), cv2.IMREAD_GRAYSCALE)  # в оперативной памяти
    # img2 = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow("Display window", img)
    cv2.waitKey(0)


def change_to_bw_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"), cv2.IMREAD_GRAYSCALE)  # в оперативной памяти
    # img2 = cv2.imread(path, cv2.IMREAD_COLOR)
    # image_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
    contrast = 90
    image = cv2.threshold(img, contrast, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Display window", image)
    cv2.waitKey(0)


def change_quality_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"), cv2.IMREAD_COLOR)
    quality = 70
    cv2.imwrite("src_avatar.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, quality])


def resize_image():
    img = cv2.imread(cv2.samples.findFile("src.jpg"), cv2.IMREAD_COLOR)
    height, width, channels = img.shape  # (1920, 1080, 3)
    multiply: float = 75 / 100  # 1.0 = 100%
    img2 = cv2.resize(img, (int(width * multiply), int(height * multiply)))
    cv2.imshow("Display img", img)
    cv2.imshow("Display img2", img2)
    cv2.waitKey(0)



"""
Сжиматель аватарок для облака.

input(10 files) -> 1920:1080 (100%) = 3.0 mb
output(10 files) -> 1920*s_param:1080*s_param (100 * q_param%) = 3.0/N mb
"""

#
#
#
