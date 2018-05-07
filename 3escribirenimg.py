import numpy as np
import cv2

img = cv2.imread('fotomarcador.jpg',cv2.IMREAD_COLOR)

#linea
cv2.line(img,(0,0), (150,150), (255,0,0), 15) #imagen, punto inicio, punto final, color, ancho

#rectangulo
cv2.rectangle(img, (15,25), (200,150),(255,150,0) ,5) #imagen, punto inicio, vertice opuesto, color, ancho

#circulo
cv2.circle(img,(100,63), 55,(0,150,255), 20) #imagen, centro, radio, color, ancho
cv2.circle(img,(300,63), 55,(0,0,255), -1) #circulo relleno

#poligono
pts= np.array([ [200,3],[200,40],[40,300],[300,50] ],np.int32)
#pts = pts.reshape((-1,-1,2))
cv2.polylines(img,[pts],True,(0,255,255),3) #imagen, puntos, opcion para cerrar los puntos al final, color

#escritura
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,    'TEST',(500,30),      font,    1,     (0,0,0),2,      cv2.LINE_AA)
            #imagen, texto, punto inicial, fuente, tamaño, color, grosor, tipo linea

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
