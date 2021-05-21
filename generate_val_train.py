#  检验.txt 对应的.jpg或.jpeg或.png文件是否存在、是否可读（此处调用了cv2库）
#  按照训练集和验证机的比例，生成train.txt和val.txt

import os
import random
import cv2

# 默认img和txt在同一个文件夹
path='obj'

# 训练集:测试集 = 0.85:0.15
ratio=0.85

def check(img_path):
    # 判断文件是否可读
    image=cv2.imread(img_path)
    if image is None:
        return False
    else:
        return True

def main():
    filenames=os.listdir(path)
    # txt目标注释文件列表
    annoList=[]
    for file in filenames:
        # 文件名
        name=file.split('.')[0]
        # 文件后缀
        suffix=file.split('.')[-1]
        # 是图片
        if suffix in ['jpg','jpeg','png']:
            # 如果没有安装python版cv2，且确定图片无损坏，则注释此行、import cv2、check()即可。
            assert check(path + '/' + file)==True, '%s is unreadable'%(file)
            # 图片对应的txt文件
            anno= name + '.txt'
            if os.path.isfile(path + '/'+ anno):
                annoList.append(file)
            else:
                print('%s without annotation file' %(file) )
    # 乱序
    random.shuffle(annoList)
    length=len(annoList)
    # 训练集
    f=open('./train.txt','w')
    for anno in annoList[:int(ratio*length)]:
        f.write('./data/' + path + '/' + anno + '\n')
    f.close()
    # 测试集
    f=open('./val.txt','w')
    for anno in annoList[int(ratio*length):]:
        f.write('./data/' + path + '/' + anno + '\n')
    f.close()

if __name__=='__main__':
    main()
    print('generate trainval.txt success')
