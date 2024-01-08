import paddlex as pdx
import cv2
import json
import numpy as np

import os
def predict_result(image):
    retval = os.getcwd()
    os.chdir(retval+'\paddlex_mobilenetv3\jiejun')
    # print("Loading model...")
    model = pdx.load_model('inference_model\inference_model')
    # print("Model loaded.")

    im = cv2.imread(image)
    im = im.astype('float32')

    result = model.predict(im)
    if (result[0]['category']=="no"):
        cat_result= "无接菌"
        other_result="有接菌"
    if (result[0]['category'] == "yes"):
        cat_result = "有接菌"
        other_result= "无接菌"
    # 输出分类结果
    if model.model_type == "classifier":
        # print(result)
        str1= "By CNN-MobileNetV3\n"+"the Probability of "+str(cat_result)+" is "+str(round((100*result[0]['score']),2))+"%,"+ str(other_result) +" is "+str(round((100*(1-result[0]['score'])),2))+"%"
        # return (str1)

# 掺假判定↓
    os.chdir(retval+'\paddlex_mobilenetv3\chanjia')
    # print("Loading model...")
    model = pdx.load_model('inference_model\inference_model')
    # print("Model loaded.")

    im = cv2.imread(image)
    im = im.astype('float32')

    result = model.predict(im)
    if (result[0]['category'] == "high"):
        cat_result2 = "高掺假"
        other_result2 = "低掺假"
    if (result[0]['category'] == "low"):
        cat_result2 = "低掺假"
        other_result2 = "高掺假"
    # 输出分类结果
    if model.model_type == "classifier":
        # print(result)
        str2 = "\nthe Probability of " + str(cat_result2) + " is " + str(
            round((100 * result[0]['score']), 2)) + "%," + str(other_result2) + " is " + str(
            round((100 * (1 - result[0]['score'])), 2)) + "%"
        return str1+str2
# import paddlex as pdx
        # print(result[0]['category'])
        # print(result[0]['score'])
    # 可视化结果, 对于检测、实例分割务进行可视化
    # if model.model_type == "detector":
    #     # threshold用于过滤低置信度目标框
    #     # 可视化结果保存在当前目录
    #     pdx.det.visualize(im, result, threshold=0.5, save_dir='./')
    #
    # # 可视化结果, 对于语义分割务进行可视化
    # if model.model_type == "segmenter":
    #     # weight用于调整结果叠加时原图的权重
    #     # 可视化结果保存在当前目录
    #     pdx.seg.visualize(im, result, weight=0.0, save_dir='./')
if __name__ == '__main__':
    result=predict_result("E:/Resize_Photo/Original/J-100%-3.JPG")
    print(result)