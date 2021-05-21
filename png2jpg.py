import os

import cv2
from PIL import Image
import numpy as np
#测试代码用Opencv读取图片并显示
# img = cv2.imread('../images/smile/1.jpg')
# cv2.imshow('img',img)
# cv2.waitKey(0)



 


def mytest():
    for i in range(799):
        print(i+1)
        # = str(i+1)
        # = "get_image/".join( num) +".png"
        path = "%s%d%s"%("get_image/", i+1, ".png")
        frontstr =path.split('/')
        backend =  frontstr[1].split('.')
        print("frontstr = ",frontstr)
        print("backend = ",backend)

        name = backend[0]
        format = backend[1]
        if(format == "png"):
            I = Image.open(path) 
            #I.show()
            I.save("jpg/" + name +".jpg")
        

def listfiles(rootDir):
    # 读取根目录下所有目录和文件
    list_dirs = os.listdir(rootDir)
    cur_dir = os.getcwd()
    #("cur_dir =", cur_dir)
    # 遍历根目录下所有的目录和所有文件
    for f in list_dirs:
        #print("f = ", f)
        leifid =f.split('.')[0]
        endstr = f.split('.')[1]
        if(endstr == "png"):
            filepath = os.path.join(cur_dir,f)
            print("filepath =", filepath)
        # 防止有异常图片（不完整图片）如果有就删除
            src = cv2.imread(filepath,1)
            if(src != None):
                cv2.namedWindow("Image")
                cv2.imshow("Image", src)
        #print('src=',filepath,src.shape)
        # 移除原有图片路径把图片更改格式保存
        #os.remove(filepath)
            jpgname = os.path.join(cur_dir,fileid+'.jpg')
            print("jpgname = ",jpgname)
            cv2.imwrite(jpgname,src)
            
                
if __name__ == '__main__':
    mytest()
    #listfiles('obj/')
