This Python program is developed in order to open an internal camera and display the image within Tkinter window.

 
#importing modules required
from ttk import *
import Tkinter as tk
from Tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np


global last_frame                                      #creating global variable
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)
global cap
cap = cv2.VideoCapture(0)

def show_vid():                                        #creating a function
    if not cap.isOpened():                             #checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if flag is None:
        print "Major error!"
        # <code to handle exception>
    elif flag:
        global last_frame
        last_frame = frame.copy()

    pic = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)

if __name__ == '__main__':
    root=tk.Tk()                                     #assigning root variable for Tkinter as tk
    lmain = tk.Label(master=root)
    lmain.grid(column=0, rowspan=4, padx=5, pady=5)
    root.title("Sign Language Processor")            #you can give any title
    show_vid()
    root.mainloop()                                  #keeps the application in an infinite loop so it works continuosly
    cap.release()
