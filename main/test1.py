import os
import  requests
import base64
import json
from pprint import pprint
import time
import io
from io import BytesIO
import  cv2
import numpy as np
from PIL import Image
import glob

#client_id 为官网获取的AK， client_secret 为官网获取的SK
api_key = '0YZIGdYEo8mgrxM5xQA0kmGG'
secret_key = 'YVo4mqQzCkvbpRVG6Hkh01xWDmvfP1IP'

class Traffic_flowRecognizer(object):
    def __init__(self,api_key,secret_key):
        self.access_token = self._get_access_token(api_key=api_key, secret_key=secret_key)
        self.API_URL = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect'+'?access_token' \
                       + self.access_token
        #获取token
        @staticmethod
        def _get_access_token(api_key, secret_key):
            api = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
                  '&client_id={}&client_secret={}'.format(api_key, secret_key)
            rp = requests.post(api)
            if rp.ok:
                rp_json = rp.json()
                print(rp_json['access_token'])
                return rp_json['access_token']
            else:
                print('=> Error in get aeecss token')
        def get_result(self,params):
            rp = requests.post(self.API_URL,data=params)
            if rp.ok:
                print('=> Success! got result: ')
                rp_json = rp.json()
                pprint(rp_json)
                return rp_json
            else:
                print('=> Error! token invalid or network error!')
                print(rp.content)
                return None
        #识别车流量
        def detect(self):

            ###对视频进行抽帧后，连续读取图片,下一步就是将视频处理成每一帧的图片，然后传入到该程序中
            WSI_MASK_PATH = 'C:\\Users\\sh\\Desktop\\车辆识别检测'#存放图片的文件夹路径
            paths = glob.glob(os.path.join(WSI_MASK_PATH,'*.jpg'))
            paths.sort()
            data_list = []
            c = 1
            for path in paths:
                f = open(path,'rb')
                img_str = base64.b64encode(f.read())
                data_list.append(img_str)
                params = {'area':'1,269,400,269,400,180,1,180','case_id':1214,'case_init':'false','image':data_list,'show':'true'}
                tic = time.clock()
                rp_json = self.get_result(params)
                toc = time.clock()
                print('单次处理时长: '+'%.2f'  %(toc - tic) +' s')
                img_b64encode = rp_json['image']
                img_b64encode = base64.b64encode(img_b64encode)#base64解码
                #显示检测结果图片
                image = io.BytesIO(img_b64encode)
                img = Image.open(img)
                img.show()
                #存储检测结果图片
                file = open('C:\\Users\\sh\\Desktop\\车辆识别检测\\out'+str(c)+'.jpg','wb')
                file.write(img_b64encode)
                file.close()
                c = c+1

if __name__ == '__main__':
    recognizer = Traffic_flowRecognizer(api_key, secret_key)
    recognizer.detect()