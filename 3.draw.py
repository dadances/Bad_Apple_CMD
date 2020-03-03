import os
import cv2
import time
import numpy

def main():
    frames = input('帧率：')
    dir=frames+'//text'
    bad_apple=[]
    total=os.listdir(dir).__len__()
    for num in range(1,total+1):
        bad_apple.append(open(dir+'//pic_'+str(num)+'.jpg.txt','r').read())
    for num in range(total):
        print(bad_apple[num])
        time.sleep(0.01)

if __name__ == '__main__':
    main()

