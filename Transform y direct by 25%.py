import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read img and convert color

img = cv.imread(r'C:\Users\KarthickRaja\Desktop\images.jpg')


cv.imshow("Here",img)


def translate_1(img,x,y):
    tranmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])   #1-width 0-Heigth
    return cv.warpAffine(img,tranmat,dimensions)

translate_1=translate_1(img,0,25)

cv.imshow("y direc by 25%",translate_1)

cv.waitKey(0)



cv.imwrite("Transform_y.jpg",translate_1)

print("Saved sucessfully")