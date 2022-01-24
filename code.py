#backup2
from tkinter import *
import tkinter
import tkinter.font as font
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import numpy
# =================================================================================================================================================
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
def pro(image11):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hand=mp_hands.Hands(max_num_hands=2,min_detection_confidence=0.7, min_tracking_confidence=0.7)
    cap=cv2.VideoCapture(0)

    # filename = 'PngItem_555040.png'
    filename = image11
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    while True:
        ret,photo = cap.read()
        results=hand.process(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))
        if results.multi_handedness:
    #         print('Handedness:', results.multi_handedness)
    #         print(results.multi_hand_landmarks
            for hand_landmarks in results.multi_hand_landmarks:
    #             mp_drawing.draw_landmarks(photo, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                h,w,c = photo.shape
                for ids , ss in enumerate(hand_landmarks.landmark):
    #                 cv2.line(photo ,(300,0),(int(ss.x*w),int(ss.y*h)),(0, 70, 255), 2)

                    if ids == 18:
    #                     cv2.circle(photo,(int(ss.x*w),int(ss.y*h)) , 10, (23, 40, 246), 5)
                        x1=int(ss.x*w)
                        y1=int(ss.y*h)-10
    #                     print(x1,":",y1,"....")
                    if ids==2:
                        x2=int(ss.x*w)
                        y2=int(ss.y*h)+40
    #                     print("....",x2,",",y2)
    #                     cv2.circle(photo,(int(ss.x*w),int(ss.y*h)) , 10, (23, 40, 246), 5)

            try:
    #             cv2.rectangle(photo, (x1,y1), (x2,y2), (0, 70, 255), 2)
                cphoto = photo[y1:y2, x1:x2]
    #             cv2.imshow('hiii',cphoto)
                if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                    img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
        #             photo[y1:y2, x1/:x2]=img
                    photo = Image.fromarray(photo)
                    photo.paste(img, (x1,y1), img)
                    photo = numpy.asarray(photo)
                    cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
    #                 cv2.imshow('hi',photo)
            except:
                pass

        photo = cv2.flip(photo, 1)
        out.write(photo)
        cv2.imshow('hi',photo)
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
    cap.release()
    cv2.destroyAllWindows()

def a1():
    pro("imgbin_ganesha-asian-elephant-mehndi-png.png")
def a2():
    pro("5a21ab29634b23.4184185415121559454067.png")
def a3():
    pro("imgbin_henna-mehndi-cut-flowers-art-png.png")
def a4():
    pro("imgbin_mandala-coloring-book-drawing-yin-and-yang-symbol-png.png")
def a5():
    pro("imgbin_mehndi-henna-mandala-png.png")
def a6():
    pro("PngItem_555040.png")
def recod():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
# ------------------------------------------------------------------------------------------------------------------------------------------------
top = tkinter.Tk()
width= top.winfo_screenwidth() 
height= top.winfo_screenheight()
#setting tkinter window size
top.geometry("%dx%d" % (width, height))
top.configure(background='black')
top.title('SWS Filters...')


myFont1 = font.Font(size=30,weight='bold') 
l1 = Label(top, text = "SWS Filters...", bg = "black",fg="red",font=10)
l1.pack()
l1['font'] = myFont1
l1.place(x = 40,y = 20)


myFont1 = font.Font(size=20,weight='bold') 
l2 = Label(top, text = "Hand Filters:-", bg = "black",fg="red",font=10)
l2.pack()
l2['font'] = myFont1
l2.place(x = 40,y = 90)

image1 = Image.open("imgbin_ganesha-asian-elephant-mehndi-png.png")
resize_image1 = image1.resize((150, 150))
img1 = ImageTk.PhotoImage(resize_image1)

a1 = Button(top, text = "Red1", fg = "red", image = img1,command =a1)
a1.pack()
a1.place(x = 40,y = 150,height=150,width=150)
image = Image.open("5a21ab29634b23.4184185415121559454067.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)
a2 = Button(top, text = "Red", fg = "red",image = img,command=a2)
a2.pack()
a2.place(x = 210,y =150,height=150,width=150)
image2 = Image.open("imgbin_henna-mehndi-cut-flowers-art-png.png")
resize_image2 = image2.resize((150, 150))
img2 = ImageTk.PhotoImage(resize_image2)
a3 = Button(top, text = "Red", fg = "red",image = img2,command=a3)
a3.pack()
a3.place(x = 380,y =150,height=150,width=150)
image3 = Image.open("imgbin_mandala-coloring-book-drawing-yin-and-yang-symbol-png.png")
resize_image3 = image3.resize((150, 150))
img3 = ImageTk.PhotoImage(resize_image3)
a1 = Button(top, text = "Red1", fg = "red",image = img3,command=a4)
a1.pack()
a1.place(x = 550,y = 150,height=150,width=150)
image4 = Image.open("imgbin_mehndi-henna-mandala-png.png")
resize_image4 = image4.resize((150, 150))
img4 = ImageTk.PhotoImage(resize_image4)
a2 = Button(top, text = "Red", fg = "red",image = img4,command=a5)
a2.pack()
a2.place(x = 720,y =150,height=150,width=150)
image5 = Image.open("PngItem_555040.png")
resize_image5 = image5.resize((150, 150))
img5 = ImageTk.PhotoImage(resize_image5)
a3 = Button(top, text = "Red", fg = "red",image = img5,command=a6)
a3.pack()
a3.place(x = 890,y =150,height=150,width=150)
# top.mainloop()---------------------------------------------------------------------------------------------------
def blackpenther():

    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'blackpanther.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-20
            y1 =loc[0][1]-60
            x2 =loc[0][2]+x1+30
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
    
    
def ironman():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Open Webcam
    filename = '580b57fbd9996e24bc43c051.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-50
            y1 =loc[0][1]-40
            x2 =loc[0][2]+x1+110
            y2 =loc[0][3]+y1+90
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(1) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()

def spiderman():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Open Webcam
    filename = 'spider.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-20
            y1 =loc[0][1]-60
            x2 =loc[0][2]+x1+30
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
def jocker():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'PngItem_2481622.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-20
            y1 =loc[0][1]-60
            x2 =loc[0][2]+x1+50
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
    
def hacker1():
        #spider Man
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'anonymous-mask-png-5331.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-50
            x2 =loc[0][2]+x1+60
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
def cross():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = '314641366357211.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-30
            x2 =loc[0][2]+x1+60
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
    
myFont1 = font.Font(size=20,weight='bold') 
l2 = Label(top, text = "Face Filters:-", bg = "black",fg="red",font=10)
l2.pack()
l2['font'] = myFont1
l2.place(x = 40,y = 330)

image11 = Image.open("blackpanther.png")
resize_image11 = image11.resize((150, 150))
img11 = ImageTk.PhotoImage(resize_image11)

a1 = Button(top, text = "Red1", fg = "red", image = img11,command =blackpenther)
a1.pack()
a1.place(x = 40,y = 390,height=150,width=150)
image12 = Image.open("580b57fbd9996e24bc43c051.png")
resize_image12 = image12.resize((150, 150))
img12 = ImageTk.PhotoImage(resize_image12)
a2 = Button(top, text = "Red", fg = "red",image = img12,command=ironman)
a2.pack()
a2.place(x = 210,y =390,height=150,width=150)
image13 = Image.open("spider.png")
resize_image13 = image13.resize((150, 150))
img13 = ImageTk.PhotoImage(resize_image13)
a3 = Button(top, text = "Red", fg = "red",image = img13,command=spiderman)
a3.pack()
a3.place(x = 380,y =390,height=150,width=150)
image14 = Image.open("PngItem_2481622.png")
resize_image14 = image14.resize((150, 150))
img14 = ImageTk.PhotoImage(resize_image14)
a1 = Button(top, text = "Red1", fg = "red",image = img14,command=jocker)
a1.pack()
a1.place(x = 550,y = 390,height=150,width=150)
image15 = Image.open("anonymous-mask-png-5331.png")
resize_image15 = image15.resize((150, 150))
img15 = ImageTk.PhotoImage(resize_image15)
a2 = Button(top, text = "Red", fg = "red",image = img15,command=hacker1)
a2.pack()
a2.place(x = 720,y =390,height=150,width=150)
image16 = Image.open("314641366357211.png")
resize_image16 = image16.resize((150, 150))
img16 = ImageTk.PhotoImage(resize_image16)
a3 = Button(top, text = "Red", fg = "red",image = img16,command=cross)
a3.pack()
a3.place(x = 890,y =390,height=150,width=150)
# ----------------------------------------------------------------------------------------------------------------------

def emoji1():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'YourPng.com - 700x700.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-30
            x2 =loc[0][2]+x1+80
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()

def emoji2():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'troll-face-png-19697.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-30
            x2 =loc[0][2]+x1+60
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
def emoji3():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'toppng.com-ew-smiley-bomb-smiley-580x480.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-10
            y1 =loc[0][1]-30
            x2 =loc[0][2]+x1+80
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
def emoji4():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = 'toppng.com-smiley-face-vector-clip-art-smiley-face-color-blue-600x599.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-10
            y1 =loc[0][1]-30
            x2 =loc[0][2]+x1+30
            y2 =loc[0][3]+y1+85
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
def emoji5():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = '[PXPNG.COM]Download Blue Emoji Transparent Background - 512x512.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-50
            x2 =loc[0][2]+x1+70
            y2 =loc[0][3]+y1+95
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
    
def emoji6():
    face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename = '[PXPNG.COM]Download Cute Blue Emoji Background PNG - 512x512.png'
    frontImage = Image.open(filename)
    frontImage = frontImage.convert("RGBA")
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
        loc = face_model.detectMultiScale(photo)
    #     photo1 = photo
        if len(loc) == 1:
            x1 =loc[0][0]-30
            y1 =loc[0][1]-50
            x2 =loc[0][2]+x1+70
            y2 =loc[0][3]+y1+95
            cphoto = photo[y1:y2, x1:x2]
            if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
                img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
    #             photo[y1:y2, x1/:x2]=img
                photo = Image.fromarray(photo)
                photo.paste(img, (x1,y1), img)
                photo = numpy.asarray(photo)
            cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
            photo = cv2.flip(photo, 1)
            cv2.imshow('hi',photo)

            if cv2.waitKey(10) == 13: #13 is the Enter Key
                break

    cap.release()
    cv2.destroyAllWindows()
    
myFont1 = font.Font(size=20,weight='bold') 
l2 = Label(top, text = "Emoji Filters:-", bg = "black",fg="red",font=10)
l2.pack()
l2['font'] = myFont1
l2.place(x = 40,y = 570)

image21 = Image.open("YourPng.com - 700x700.png")
resize_image21 = image21.resize((150, 150))
img21 = ImageTk.PhotoImage(resize_image21)

a1 = Button(top, text = "Red1", fg = "red", image = img21,command =emoji1)
a1.pack()
a1.place(x = 40,y = 630,height=150,width=150)
image22 = Image.open("troll-face-png-19697.png")
resize_image22 = image22.resize((150, 150))
img22 = ImageTk.PhotoImage(resize_image22)
a2 = Button(top, text = "Red", fg = "red",image = img22,command=emoji2)
a2.pack()
a2.place(x = 210,y =630,height=150,width=150)
image33 = Image.open("toppng.com-ew-smiley-bomb-smiley-580x480.png")
resize_image33 = image33.resize((150, 150))
img33 = ImageTk.PhotoImage(resize_image33)
a3 = Button(top, text = "Red", fg = "red",image = img33,command=emoji3)
a3.pack()
a3.place(x = 380,y =630,height=150,width=150)
image44 = Image.open("toppng.com-smiley-face-vector-clip-art-smiley-face-color-blue-600x599.png")
resize_image44 = image44.resize((150, 150))
img44 = ImageTk.PhotoImage(resize_image44)
a1 = Button(top, text = "Red1", fg = "red",image = img44,command=emoji4)
a1.pack()
a1.place(x = 550,y = 630,height=150,width=150)
image45 = Image.open("[PXPNG.COM]Download Blue Emoji Transparent Background - 512x512.png")
resize_image45 = image45.resize((150, 150))
img45 = ImageTk.PhotoImage(resize_image45)
a2 = Button(top, text = "Red", fg = "red",image = img45,command=emoji5)
a2.pack()
a2.place(x = 720,y =630,height=150,width=150)
image26 = Image.open("[PXPNG.COM]Download Cute Blue Emoji Background PNG - 512x512.png")
resize_image26 = image26.resize((150, 150))
img26 = ImageTk.PhotoImage(resize_image26)
a3 = Button(top, text = "Red", fg = "red",image = img26,command=emoji6)
a3.pack()
a3.place(x = 890,y =630,height=150,width=150)
top.mainloop()