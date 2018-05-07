import tkinter
import cv2
import PIL.ImageTk,PIL.Image
import time

face_cascade = cv2.CascadeClassifier('haarcascadefrontalfacedefault.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascadeeye.xml')

class MyVideoCapture():
    def __init__(self,video_source=0):
        #abrir el canal
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("No disponible para abrir video",video_source)

        #obtener tamaño
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()

    def get_frame(self):
        if self.vid.isOpened():
            ret,frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)
        else:
            return (None)

class App():
    def __init__(self,window,window_title,video_source=0):
        self.window = window
        self.window.title(window_title)

        self.btn_start = tkinter.Button(window, text="Inicio", width=50, command= lambda: self.iniciar(video_source,window))
        self.btn_start.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()


    def iniciar(self,video_source,window):
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        # botones
        self.btn_snapshot = tkinter.Button(window, text="Captura", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        self.delay = 15
        self.update()


    def snapshot(self):
        ret, frame = self.vid.get_frame()

        self.deteccion(frame)

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))


    def update(self):

        ret,frame = self.vid.get_frame()

        if ret:
            self.deteccion(frame)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0,image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay,self.update)

    def deteccion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = eyes_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


#crear una ventana y pasarla al objeto tipo app
App(tkinter.Tk(),"Tkinter y openCV")
