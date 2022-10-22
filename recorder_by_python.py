from turtle import width
import cv2
import pyautogui as py
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height_1 = GetSystemMetrics(1)
dim = (width,height_1)
#--------------------------------------
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("play.mp4",f,30.0,dim)
start_now_time = time.time()
dur = 10 #time of video extra 4 is gives for addition 
end_time = start_now_time + dur
#--------------------------------------
while True:
    image = py.screenshot()
    frame_a = np.array(image)
    frame_1 = cv2.cvtColor(frame_a,cv2.COLOR_BGR2RGB)
    output.write(frame_1)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print("-----END-----")


