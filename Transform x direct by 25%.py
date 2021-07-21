import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read img

img = cv.imread(r'C:\Users\KarthickRaja\Desktop\images.jpg')


cv.imshow("Input_image",img)

#Transform to +x direction by 25%

def translate(img,x,y):
    tranmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])   #1-width 0-Heigth
    return cv.warpAffine(img,tranmat,dimensions)


translate=translate(img,25,0)

cv.imshow("x direc by 25%",translate)

cv.waitKey(0)


cv.imwrite("Transform_x.jpg",translate)

print("Saved sucessfully")