import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #filtro por color
    lower_pink = np.array([150,150,50])
    upper_pink = np.array([180,255,250])

    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    #blurring
    kernel = np.ones((15,15) , np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)

    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median',median)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()