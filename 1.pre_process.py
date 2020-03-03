import os
import cv2
import shutil
import time

#初始化路径
def ini_path(frame):
    if os.path.exists(frame):
        shutil.rmtree(frame,True)
    os.system('mkdir '+frame+'\\img')
    os.system('mkdir '+frame+'\\gray')
    os.system('mkdir '+frame+'\\binary')
    os.system('mkdir ' + frame + '\\pool')
    os.system('mkdir ' + frame + '\\text')
#裁剪视频
def ffmpeg(frame):
    com='ffmpeg -i badapple.mp4 -r '+frame+' -q:v 2 -f image2 '+frame+'/img/pic_%d.jpg'
    os.system(com)
#得到灰度图
def get_gray(img_name,frame):
    img_path=frame+'\\img\\'+img_name
    img_gray = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(frame+'\\gray\\'+img_name,img_gray)
    return img_gray
#得到二值图
def get_binary(img,img_name,frame):
    ret,img_binary=cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    cv2.imwrite(frame+'\\binary\\'+img_name,img_binary)
    return img_binary

def main():
    frames=input('帧率：')
    start=time.time()
    ini_path(frames)
    ffmpeg(frames)
    for name in os.listdir(frames+'/img'):
        img_gray=get_gray(name,frames)
        img_binary=get_binary(img_gray,name,frames)
    end=time.time()
    print('Pre process Finish! Process time:',end-start)

if __name__ == '__main__':
    main()