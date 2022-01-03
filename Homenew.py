from tkinter import * # user interface design
import tkinter # user interface design
import cv2 #opencv library for dip designed by intel
from imutils.video import VideoStream #used to read stream from camera
import time #delay
from PIL import Image,ImageTk #convertion between libraries
import numpy as np #numpy number python
import math
import pyttsx3
from tkinter import messagebox

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Home_Gesture(root)
    root.mainloop() # tk inter initilization



class Home_Gesture:
    def __init__(self, top=None): #constructor
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 16 -weight bold -slant " \
                 "roman -underline 1 -overstrike 0"
        self.count1=0
        self.count2=0
        self.count3=0
        self.count4=0
        self.count5=0
        top.geometry("1802x918+43+69")
        top.title("Samvad")
        top.configure(background="#408080")
        self.engine = pyttsx3.init()

        print("Starting Object Detection Mode")
        # start the video stream thread
        print("[INFO] starting video stream thread...")
        #self.vs = VideoStream(src=0).start() # camera initialization
        self.cap = cv2.VideoCapture(0)
        # vs = VideoStream(usePiCamera=True).start()
        time.sleep(1) #pause main thread

        self.flghsv=0
        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.19, relheight=0.34
                , relwidth=0.22)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Controls''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(width=390)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.0, rely=0.19, height=42, width=288)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Camera Interface''')
        self.Button1.configure(width=288)
        self.Button1.configure(command=self.camera_interface)



        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.14, rely=0.44, height=42, width=200)
        self.Label4.configure(background="#408080")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(text='''Count''')
        self.Label4.configure(width=597)


        self.Label1 = Label(top)
        self.Label1.place(relx=0.34, rely=0.03, height=31, width=597)
        self.Label1.configure(background="#408080")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Samvad''')
        self.Label1.configure(width=597)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.34, rely=0.10, height=31, width=597)
        self.Label5.configure(background="#408080")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(text='''Msg''')
        self.Label5.configure(width=597)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.27, rely=0.19, relheight=0.64
                , relwidth=0.43)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Detection Finger Count''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=600)

        self.Label2 = Label(self.Labelframe2)
        self.Label2.place(relx=0.0, rely=0.0, height=520, width=625)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''''')
        self.Label2.configure(width=587)

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.74, rely=0.19, relheight=0.34
                , relwidth=0.23)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Masking''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")
        self.Labelframe3.configure(width=600)

        self.Label3 = Label(self.Labelframe3)
        self.Label3.place(relx=0.0, rely=0.0, height=200, width=200)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=587)



    def camera_interface(self):
        try:
            #camera interfacing
            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 1)   #read frame from camera
            if frame is not None:

                kernel = np.ones((3, 3), np.uint8)
                roi = frame[100:300, 100:300]
                cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                #preprocessing and color range filter apply
                lower_skin = np.array([0, 20, 70], dtype=np.uint8)
                upper_skin = np.array([20, 255, 255], dtype=np.uint8)
                mask = cv2.inRange(hsv, lower_skin, upper_skin)
                qmask = cv2.dilate(mask, kernel, iterations=4)
                mask = cv2.GaussianBlur(mask, (5, 5), 100)
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # find contour of max area(hand)
                cnt = max(contours, key=lambda x: cv2.contourArea(x))

              # hull and convexity find
                epsilon = 0.0005 * cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)
                hull = cv2.convexHull(cnt)
                areahull = cv2.contourArea(hull)
                areacnt = cv2.contourArea(cnt)
                arearatio = ((areahull - areacnt) / areacnt) * 100
                hull = cv2.convexHull(approx, returnPoints=False)
                defects = cv2.convexityDefects(approx, hull)

                # l = no. of defects
                #convexity defects calculation
                l = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(approx[s][0])
                    end = tuple(approx[e][0])
                    far = tuple(approx[f][0])
                    pt = (100, 180)
                    # find length of all sides of triangle
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    s = (a + b + c) / 2
                    ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

                    d = (2 * ar) / a

                    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                    if angle <= 90 and d > 30:
                        l += 1
                        cv2.circle(roi, far, 3, [255, 0, 0], -1)

                    # draw lines around hand
                    cv2.line(roi, start, end, [0, 255, 0], 2)
                l += 1
                #b, g, r = cv2.split(frame)
                #frame = cv2.merge((r, g, b))


                #finger counting and operation perform
                if l == 1:
                    self.count2=0
                    self.count3=0
                    self.count4=0
                    self.count5=0
                    if areacnt < 2000:
                        self.Label5.configure(text='''Put hand in the box''')


                    else:
                        if arearatio < 12:
                            self.Label4.configure(text='''0''')
                        else:
                            self.Label4.configure(text='''1''')
                            self.count1 = self.count1 + 1
                            if self.count1 > 10:
                                messagebox.showinfo("Message","I am hungry")
                                self.engine.say("I am hungry")
                                self.engine.runAndWait()
                                print("Execute 1")
                                self.count1 = 0


                elif l == 2:
                    self.count1 = 0
                    self.count3 = 0
                    self.count4 = 0
                    self.count5 = 0
                    self.Label4.configure(text='''2''')
                    self.count2 = self.count2 + 1
                    if self.count2 > 10:
                        messagebox.showinfo("Message", "I want to drink water")
                        self.engine.say("I want to drink water")
                        self.engine.runAndWait()
                        print("Execute 2")
                        self.count2 = 0

                elif l == 3:
                    self.count1 = 0
                    self.count2 = 0
                    self.count4 = 0
                    self.count5 = 0
                    if arearatio < 27:
                        self.Label4.configure(text='''3''')
                        self.count3 = self.count3 + 1
                        if self.count3 > 10:
                            print("Execute 3")
                            messagebox.showinfo("Message", "I need to go to washroom")
                            self.engine.say("I need to go to washroom")
                            self.engine.runAndWait()
                            self.count3 = 0
                    else:
                        self.Label4.configure(text='''ok''')

                elif l == 4:
                    self.count1 = 0
                    self.count2 = 0
                    self.count3 = 0
                    self.count5 = 0
                    self.Label4.configure(text='''4''')
                    self.count4 = self.count4 + 1
                    if self.count4>10:
                        print("Execute 4")
                        messagebox.showinfo("Message", "I need my medicine")
                        self.engine.say("I need my medicine")
                        self.engine.runAndWait()
                        self.count4=0


                elif l == 5:
                    self.count1 = 0
                    self.count2 = 0
                    self.count3 = 0
                    self.count4 = 0
                    self.Label4.configure(text='''5''')
                    self.count5 = self.count5 + 1
                    if self.count5 > 10:
                        print("Execute 5")
                        messagebox.showinfo("Message", "I want to go out for walk")
                        self.engine.say("I want to go out for walk")
                        self.engine.runAndWait()
                        self.count5 = 0

                elif l == 6:
                    self.Label4.configure(text='''reposition''')


                else:
                    self.Label4.configure(text='''reposition''')


                #used to show images on labels
                im1 = Image.fromarray(frame)
                image = im1.resize((520, 625), Image.ANTIALIAS)
                logo1 = ImageTk.PhotoImage(image=image)
                self.Label2.configure(image=logo1)
                self.Label2.image = logo1
                im2 = Image.fromarray(mask)
                image1 = im2.resize((200, 200), Image.ANTIALIAS)
                logo2 = ImageTk.PhotoImage(image=image1)
                self.Label3.configure(image=logo2)
                self.Label3.image = logo2

                #user for perform recursion for camera
                self.Label2.after(200, self.camera_interface)


        except Exception as e:
            print(e)




if __name__ == '__main__':
    vp_start_gui() #launcher method

