import datetime

import cv2
import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp
from scipy.signal import find_peaks
import pandas as pd
import plotly.graph_objects as go
from scipy.signal import find_peaks_cwt



cap = cv2.VideoCapture('ppg_detection_video.MOV')

cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)

p1, p2 = None, None
state = 0

def get_video_duration(capture):
    fps = capture.get(cv2.CAP_PROP_FPS)
    total_no_frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    return total_no_frames / fps

def on_mouse(event, x, y, flags, userdata):
    global state, p1, p2

    # Left click
    if event == cv2.EVENT_LBUTTONUP:
        # Select first point
        if state == 0:
            p1 = (x, y)
            state += 1
        # Select second point
        elif state == 1:
            p2 = (x, y)
            state += 1
    # Right click (erase current ROI)
    if event == cv2.EVENT_RBUTTONUP:
        p1, p2 = None, None
        state = 0

video_duration = get_video_duration(cap)
cv2.setMouseCallback('Frame', on_mouse)

average_array = []
count = 0
while cap.isOpened():
    val, frame = cap.read()

    # If a ROI is selected, draw it
    if state > 1 and frame is not None:
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2)
        cropped_image = frame[p1[1]:p2[1], p1[0]:p2[0]]
        # cv2.imshow('Crop', cropped_image)
        average = np.average(cropped_image)
        average_array.append(average)
        count = count + 1

    if frame is not None:
        cv2.imshow('Frame', frame)

    key = cv2.waitKey(50)  # millisecond
    # If ESCAPE key pressed, stop
    if key == 27:
        cap.release()

y_axis = np.array(average_array)
x_axis = np.array(range(count))
peaks = find_peaks_cwt(y_axis, np.ones(y_axis.shape)*2)-1
plt.plot(x_axis, y_axis)
plt.plot(peaks, y_axis[peaks], "x")
bpm = (len(peaks)/video_duration)*60
plt.title('Beat Per Minute ' + str(bpm), loc="center")
plt.xlabel(str(datetime.datetime.now()), fontsize = 10)
plt.figure()
plt.show()
