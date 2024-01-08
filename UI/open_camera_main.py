import sys
from PyQt5 import QtGui, QtWidgets
from open_camera import Ui_MainWindow
import cv2
from PyQt5.Qt import *
import os
from Scripts.predict_mobilenetv3 import predict_result
from paddle_online.judge_functionlized import judge_Bat_and_Fake
from Scripts.crop_hough import Hough_And_Crop
from Scripts.Auto_WB import wb

class Open_Camera(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Open_Camera, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        # self.label.setScaledContents(True)  # 图片自适应
        # self.label_2.setScaledContents(True)  # 图片自适应

    def init(self):
        self.pushButton.clicked.connect(self.wb)
        self.pushButton.setEnabled(False)

        self.pushButton_2.clicked.connect(self.judge)
        self.pushButton_2.setEnabled(False)

        self.pushButton_3.clicked.connect(self.Hough)
        self.pushButton_3.setEnabled(False)
        # Clear
        self.pushButton_4.clicked.connect(self.Clear)
        # 导入图片
        self.pushButton_5.clicked.connect(self.loadphoto)

        self.pushButton_6.clicked.connect(self.MobileNetV3)
        self.pushButton_6.setEnabled(False)
        global save_path
        save_path = 'D:/temp/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)

    def Clear(self):
        self.label_3.clear()
        self.label_2.clear()
        self.label.clear()
        self.textBrowser.clear()
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_6.setEnabled(False)

    def loadphoto(self):
        global fname
        self.textBrowser.clear()
        fname, _ = QFileDialog.getOpenFileName(self, '请您选择图片', "E:/", 'Image files(*.jpg *.JPG *.gif *.png*.bmp)')
        img = QtGui.QPixmap(fname)
        img.save(save_path+"original.jpg","JPG",100)
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(img)
        self.pushButton.setEnabled(True)
        self.textBrowser.append(fname)

    def wb(self):
        image_original_path= save_path+"original.jpg"
        image = wb(image_original_path)
        cv2.imwrite(save_path+'White_Balance.jpg', image)
        imgShow = QPixmap(save_path+'White_Balance.jpg')
        self.label.setScaledContents(True)
        self.label.setPixmap(imgShow)
        self.pushButton_3.setEnabled(True)

    def Hough(self):
        image_path=save_path+'White_Balance.jpg'
        Hough_And_Crop(image_path,save_path)
        global file_path
        file_path = save_path+'Hough_No_Circle.jpg'
        imgShow = QPixmap(file_path)
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(imgShow)
        self.pushButton_2.setEnabled(True)
        self.pushButton_6.setEnabled(True)

    def MobileNetV3(self):
        string_result=predict_result(file_path)
        self.textBrowser.append(" ")
        self.textBrowser.append(string_result)

    def judge(self):
        result_str=judge_Bat_and_Fake(file_path)
        self.textBrowser.append(" ")
        self.textBrowser.append(result_str)

if __name__ == '__main__':
    from PyQt5 import QtCore

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率

    app = QtWidgets.QApplication(sys.argv)
    ui = Open_Camera()
    ui.show()
    sys.exit(app.exec_())


