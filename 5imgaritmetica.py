import numpy as np
import cv2


img1 = cv2.imread('3d1.png')
img2 = cv2.imread('3d2.png')

#superponer por adicion
add= img1+img2

#superponer con metodos de cv2
add2 = cv2.add(img1,img2)

#superponer por cantidad de saturacion de cada imagen, con 0 en gamma
weighted = cv2.addWeighted(img1,0.6, img2, 0.4, 0)


cv2.imshow('add',add)
cv2.imshow('add2',add2)
cv2.imshow('add3', weighted)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
img1 = cv2.imread('3d1.png')
img2 = cv2.imread('mainlogo.png')

#ubicar el logo

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

#filtro
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                                 #220 es el punto minimo de comparacion si algo lo excede pasa a ser 255
ret,mask= cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)

#transparencia
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
 
cv2.imshow('res',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""