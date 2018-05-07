import numpy as np
import cv2

img = cv2.imread('fotomarcador.jpg',cv2.IMREAD_COLOR)

#por pixel

img[5,5] = [255,255,255]
px = img[55,55] #ubicacion
print(px) #retorna el color del pixel seleccionado en la imagen

"""
#por region de la imagen
img[100:200 , 100:200] = [255,255,255]
"""

#copia y pegar regiones
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face #diferencia entre pixeles de watch_face


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


