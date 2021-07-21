import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read img and convert color

img = cv.imread(r'C:\Users\KarthickRaja\Desktop\images.jpg')


cv.imshow("Input_image",img)

cv.waitKey(0)