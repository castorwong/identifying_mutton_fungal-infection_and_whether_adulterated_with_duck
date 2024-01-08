import paddlex as pdx
import cv2
import json
import numpy as np
print("Loading model...")
model = pdx.load_model(r'C:\Users\Castor_WONG\paddlex_workspace\jiejun_auged\inference_model\inference_model')
print("Model loaded.")

im = cv2.imread(r'E:/Resize_Photo/Original/CK-0%-0 (2).JPGaug_19.JPG')
im = im.astype('float32')

result = model.predict(im)

# 输出分类结果
if model.model_type == "classifier":
    print(result)
    print(result[0]['category'])
    print(result[0]['score'])
# 可视化结果, 对于检测、实例分割务进行可视化
if model.model_type == "detector":
    # threshold用于过滤低置信度目标框
    # 可视化结果保存在当前目录
    pdx.det.visualize(im, result, threshold=0.5, save_dir='./')

# 可视化结果, 对于语义分割务进行可视化
if model.model_type == "segmenter":
    # weight用于调整结果叠加时原图的权重
    # 可视化结果保存在当前目录
    pdx.seg.visualize(im, result, weight=0.0, save_dir='./')
