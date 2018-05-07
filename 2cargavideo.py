import cv2
import numpy as np

cap = cv2.VideoCapture(0) #agregar nombre de archivo de video en vez del 0 

"""
#guardar un captura de video
grab= cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',grab,20.0,(640,480))
"""
while True:
    ret, frame = cap.read()
    #filtros al frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    #grabar captura de frames
    #out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
