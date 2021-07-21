import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\KarthickRaja\Desktop\images.jpg")

cv.imshow("Original image",img)

height,width=img.shape[:2]  #Define a centre

rotate=cv.getRotationMatrix2D((width/2,height/2),-90,1) #clockwise

rotate_img=cv.warpAffine(img,rotate,(width,height))

cv.imshow("Rotated image",rotate_img)

cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite("Rotate_-90_.jpg",rotate_img)

print("Saved sucessfully")

