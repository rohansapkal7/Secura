import cv2
import winsound
from tkinter import *

root = Tk()
root.title(" Secura - Camera Motion Detector")
root.geometry("500x350")
root.minsize(500,350)
root.maxsize(500,350)
root.configure(background='#18191A')

def work():

    a = int(camvalue.get())
    framename = 'Camera ' + str(camvalue.get())
    b = radio.get()
    
    
    cam = cv2.VideoCapture(a)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        for c in contours:
            if cv2.contourArea(c) < b: #Mode limit
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            winsound.Beep(500,200)
        if cv2.waitKey(10) == ord('x'):
            break
        cv2.imshow(framename, frame1)

lab = Label(root,text='SECURA',fg='white',font=('arial' ,70,'bold'),bg='#18191A',height=0)
lab.pack()

lab2 = Label(root,text='CAMERA MOTION DETECTOR',fg='grey',font=('arial' ,16),bg='#18191A',height=0)
lab2.place(x=100,y=100)

radio = IntVar()
radio.set(1000)

rb1 = Radiobutton(root,text='Normal Mode',value=1000,variable=radio,font=('arial' ,15,'bold'),fg='green',bg='#18191A')
rb2 = Radiobutton(root,text='Z+ Mode',value=200,variable=radio,font=('arial' ,15,'bold'),fg='green',bg='#18191A')
rb1.place(x=95,y=150)
rb2.place(x=270,y=150)

lab3 = Label(root,text='Cam : ',fg='white',font=('arial' ,13,'bold'),bg='#18191A',height=0)
lab3.place(x=150,y=203)

camvalue = IntVar()

camvalue = Entry(root,width=10,font=('arial'))
camvalue.place(x=206,y=200)

start_btn = Button(root,text="START",font=('arial' ,17,'bold'),width=20,command=work,bg='green')
start_btn.place(x=103,y=250)

footer = Label(root,text="Copyright 2021-22 All rights reserved by CM6I Group-A", fg='white',bg='blue',pady=5,width=500)
footer.pack(side=BOTTOM)

root.mainloop()

