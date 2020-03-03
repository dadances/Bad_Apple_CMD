import os
import cv2
import time
import numpy


def max_pooling(img):
    if img.shape[0]%2!=0:
        img = img[0:img.shape[0] - 1, 0:img.shape[1]]
    if img.shape[1]%2!=0:
        img = img[0:img.shape[0], 0:img.shape[1] - 1]
    temp=img.reshape(int(img.shape[0]/2),2,int(img.shape[1]/2),2)
    out = temp.max(axis=(1, 3))
    return out

def pool_4(img):
    for i in range(4):
        img=max_pooling(img)
    img=img[0:img.shape[0]-1,0:img.shape[1]]
    return img

def write2txt(img,img_name,frames,symbol):
    file = open(frames + '\\text\\' + img_name + '.txt', 'a')
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if str(img[h][w])=='0':
                file.write(' ')
            else:
                file.write(symbol)
        file.write('\n')
    file.flush()
    file.close()

def main():
    frames = input('帧率：')
    symbol = input('符号：')
    binary_path=frames+'\\binary'
    start=time.time()
    for img_name in os.listdir(binary_path):
        img=cv2.imread(binary_path+'\\'+img_name,cv2.IMREAD_GRAYSCALE)
        img_pool=pool_4(img)
        cv2.imwrite(frames + '\\pool\\' + img_name, img_pool)
        write2txt(img_pool,img_name, frames, symbol)
    end=time.time()
    print("process time:",end-start)

if __name__ == '__main__':
    main()