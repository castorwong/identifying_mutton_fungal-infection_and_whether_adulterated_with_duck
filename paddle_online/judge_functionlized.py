import json
import jsonpath
import base64
import os
import requests
def judge_Bat(image):
    retval = os.getcwd()
    # 目标图片的 本地文件路径，支持jpg/png/bmp格式
    # IMAGE_FILEPATH = "D:\Hough_No_Circle.jpg"
    # 可选的请求参数
    # top_num: 返回的分类数量，不声明的话默认为 6 个
    PARAMS = {"top_num": 2}
    # 服务详情 中的 接口地址
    MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/jeijun"
    # 调用 API 需要 ACCESS_TOKEN。若已有 ACCESS_TOKEN 则于下方填入该字符串
    # 否则，留空 ACCESS_TOKEN，于下方填入 该模型部署的 API_KEY 以及 SECRET_KEY，会自动申请并显示新 ACCESS_TOKEN
    ACCESS_TOKEN = "24.274238c2927ab1f1a43d46d9b538c2ff.2592000.1669601937.282335-28142572"
    API_KEY = "vBfTdTDN80YinxwxL7s49Xr8"
    SECRET_KEY = "crCR8XrXDDxexBmCeW8TunKmCy3M3vvP"
    # print("1. 读取目标图片 '{}'".format(IMAGE_FILEPATH))
    with open(image, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_str = base64_data.decode('UTF8')
    # print("将 BASE64 编码后图片的字符串填入 PARAMS 的 'image' 字段")
    PARAMS["image"] = base64_str
    # if not ACCESS_TOKEN:
    #     print("2. ACCESS_TOKEN 为空，调用鉴权接口获取TOKEN")
    #     auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"\
    #                "&client_id={}&client_secret={}".format(API_KEY, SECRET_KEY)
    #     auth_resp = requests.get(auth_url)
    #     auth_resp_json = auth_resp.json()
    #     ACCESS_TOKEN = auth_resp_json["access_token"]
    #     print("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
    # else:
    #     print("2. 使用已有 ACCESS_TOKEN")

    # print("3. 向模型接口 'MODEL_API_URL' 发送请求")
    request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
    response = requests.post(url=request_url, json=PARAMS)
    response_json = response.json()
    response_str = json.dumps(response_json, indent=4, ensure_ascii=False)#格式调一下，成为缩进
    filename = retval+'/response_jiejun.json'
    with open(file=filename, mode='w',encoding='utf-8') as f:
        # obj：欲存储为json格式的数据，fp：欲存储的文件对象
        f.write(response_str )
    result0=json.load(open(retval+'/response_jiejun.json','r',encoding='utf-8'))
    list1=jsonpath.jsonpath(result0,'$..name')
    list2=jsonpath.jsonpath(result0,'$..score')
    # print("The Probably of",list1[0],"is",end=" ")
    # print(round(100*list2[0],2),"%,",end=" ")
    # print(list1[1],"is",end=" ")
    # print(round(100*list2[1],2),"%")
    str_bat="The Probability of "+ list1[0]+" is "+str(round(100*list2[0],2))+"%,"+list1[1]+" is "+str(round(100*list2[1],2))+"%"
     #掺假测试

    PARAMS = {"top_num": 2}
    # 服务详情 中的 接口地址
    MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/chanjia"
    # 调用 API 需要 ACCESS_TOKEN。若已有 ACCESS_TOKEN 则于下方填入该字符串
    # 否则，留空 ACCESS_TOKEN，于下方填入 该模型部署的 API_KEY 以及 SECRET_KEY，会自动申请并显示新 ACCESS_TOKEN
    ACCESS_TOKEN = "24.7cfc390ca1fa7679c8c0db66f0f53e6c.2592000.1669559308.282335-28133579"
    API_KEY = "y4KFBaoHlP006qLjHYVsV7Y1"
    SECRET_KEY = "QZYfquvWl4IAiuX03ThhfOO8F9mrLyeZ"
    # print("1. 读取目标图片 '{}'".format(IMAGE_FILEPATH))
    with open(image, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_str = base64_data.decode('UTF8')
    # print("将 BASE64 编码后图片的字符串填入 PARAMS 的 'image' 字段")
    PARAMS["image"] = base64_str
    # if not ACCESS_TOKEN:
    #     print("2. ACCESS_TOKEN 为空，调用鉴权接口获取TOKEN")
    #     auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"\
    #                "&client_id={}&client_secret={}".format(API_KEY, SECRET_KEY)
    #     auth_resp = requests.get(auth_url)
    #     auth_resp_json = auth_resp.json()
    #     ACCESS_TOKEN = auth_resp_json["access_token"]
    #     print("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
    # else:
    #     print("2. 使用已有 ACCESS_TOKEN")

    # print("3. 向模型接口 'MODEL_API_URL' 发送请求")
    request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
    response = requests.post(url=request_url, json=PARAMS)
    response_json = response.json()
    response_str = json.dumps(response_json, indent=4, ensure_ascii=False)#格式调一下，成为缩进
    filename = retval+'/response_chanjia.json'
    with open(file=filename, mode='w',encoding='utf-8') as f:
        # obj：欲存储为json格式的数据，fp：欲存储的文件对象
        f.write(response_str )
    result=json.load(open(retval+'/response_chanjia.json','r',encoding='utf-8'))
    list3=jsonpath.jsonpath(result,'$..name')
    list4=jsonpath.jsonpath(result,'$..score')

    # print("The Probably of",list3[0],"is",end=" ")
    # print(round(100*list4[0],2),"%,",end=" ")
    # print(list3[1],"is",end=" ")
    # print(round(100*list4[1],2),"%")
    str_fake="The Probability of "+list3[0]+" is "+str(round(100*list4[0],2))+"%,"+list3[1]+" is "+str(round(100*list4[1],2))+"%"
    final="By AutoDL Transfer:\n"+str_bat+"\n"+str_fake
    return final
if __name__ == '__main__':
    image_path = "D:/temp/original.jpg"
    result=judge_Bat(image_path)
    print(result)

