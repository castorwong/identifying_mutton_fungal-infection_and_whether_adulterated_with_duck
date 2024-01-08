import cv2
from PIL import Image
import numpy as np
def Hough_And_Crop(image_read,saved_path):
    image = cv2.imread(image_read)
    height, width, _ = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度图像

    blur = cv2.medianBlur(gray, 5)

    se = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10), (-1, -1))
    close = cv2.morphologyEx(blur, cv2.MORPH_OPEN, se)
    edges = cv2.Canny(close, 80, 100)
    # hough transform  规定检测的圆的最大最小半径，不能盲目的检测，否则浪费时间空间

    circle1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 500, param1=100, param2=100, minRadius=700,
                               maxRadius=900)  # 把半径范围缩小点，检测内圆，瞳孔

    # circle1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=200, maxRadius=300)
    # circle1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 500, param1=100, param2=100, minRadius=600,
    #                            maxRadius=900)  # 把半径范围缩小点，检测内圆，瞳孔

    circles = circle1[0, :, :]  # 提取为二维
    circles = np.uint16(np.around(circles))  # 四舍五入，取整
    for i in circles[:]:
        # cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 10)  # 画圆
        # cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 10)  # 画圆心
        r = int(i[2])
        x = int(i[0])
        y = int(i[1])
        S_percentage = 3.1416 * r * r / height / width * 100
        S_zoom_ratio = S_percentage / 25.0
        length_zoom_ratio = (S_zoom_ratio) ** 0.5
        # height_after = height * length_zoom_ratio
        # width_after = width * length_zoom_ratio
        # S_after = height_after * width_after

        height_after = 2*r*1.2
        width_after = 2*r*1.2

        img = Image.fromarray(np.uint8(image))

        box = (x - width_after / 2, y - height_after / 2, x + width_after / 2, y + height_after / 2)
        img = img.crop(box)
        # print(f'圆心坐标为:{(x, y)}半径为{r}像素,培养皿占整个画面的{round(S_percentage, 2)}%',end="")
        # print(f'\n培养皿的面积为{height*width}，修改后的面积为{height_after*width_after},新占比{3.1416 * r * r/height_after/width_after*100}')
        img = np.asarray(img)
    cv2.imwrite(saved_path+'Hough_No_Circle.jpg', img)
    for i in circles[:]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 10)  # 画圆
        cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 10)  # 画圆心
        r = int(i[2])
        x = int(i[0])
        y = int(i[1])
        S_percentage = 3.1416 * r * r / height / width * 100
        S_zoom_ratio = S_percentage / 25.0
        length_zoom_ratio = (S_zoom_ratio) ** 0.5
        # height_after = height * length_zoom_ratio
        # width_after = width * length_zoom_ratio
        height_after = 2*r*1.2
        width_after = 2*r*1.2
        # S_after = height_after * width_after

        img = Image.fromarray(np.uint8(image))

        box = (x - width_after / 2, y - height_after / 2, x + width_after / 2, y + height_after / 2)
        img = img.crop(box)
        # print(f'圆心坐标为:{(x, y)}半径为{r}像素,培养皿占整个画面的{round(S_percentage, 2)}%',end="")
        # print(f'\n培养皿的面积为{height*width}，修改后的面积为{height_after*width_after},新占比{3.1416 * r * r/height_after/width_after*100}')
        img = np.asarray(img)
    cv2.imwrite(saved_path+'Hough_With_Circle.jpg', img)
if __name__ == '__main__':
    Hough_And_Crop('D:/White_Balance.jpg')
    # imgShow = QPixmap('D:/Hough_With_Circle.jpg')