import cv2
from skimage import io
import numpy as np

def wb(image_path):
    image = cv2.imread(image_path)
    top = image.shape[0] * image.shape[1] * 0.05  # 改进WhitePatch中的光照强度Li
    b, g, r = cv2.split(image)
    rgbmax = [0, 0, 0]
    for i in range(3):
        sum = 0
        j = 256
        h, _ = np.histogram(cv2.split(image)[i].flatten(), 256, [0, 256])

        # BGR通道拼接成一个一维数组，BGR，共计0-255 256个量，统计范围0-255
        # 返回值hist 直方图的值
        while (sum < top) & (j > 1):  # 只要像素点个数没有统计完，并且j>1
            j = j - 1
            sum = sum + h[j]  # 累加直方图值
        rgbmax[i] = j
    b = (b / rgbmax[0] * 255).clip(0, 255)  # 规范在0,255的区间内
    g = (g / rgbmax[1] * 255).clip(0, 255)
    r = (r / rgbmax[2] * 255).clip(0, 255)
    image = cv2.merge([b, g, r]).astype(np.uint8)
    return image

if __name__ == '__main__':
    image_path = "D:/original.jpg"
    result=wb(image_path)
    cv2.imshow("result",result)
    cv2.waitKey(0)