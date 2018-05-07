import cv2
import tkinter as tk
from PIL import Image, ImageTk

face_cascade = cv2.CascadeClassifier('haarcascadefrontalfacedefault.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascadeeye.xml')

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Prueba camara")

viewFrame = tk.Frame(ventana)
viewFrame.grid(row=0, column=0)

etiFrame = tk.Label(viewFrame)
etiFrame.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def captura():
    print("entro")
    while True:
        print("entro while")
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            print("entro for 1")
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eyes_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                print("entro for2")
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        etiFrame.imgtk = imgtk
        etiFrame.configure(image=imgtk)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break



boton = tk.Button(ventana,text="Iniciar Procesamiento",command=captura).grid(row=1,column=0)

ventana.mainloop()