import cv2
import matplotlib.pyplot as plt
video=cv2.VideoCapture('./yolotest.mp4')
ret,frame=video.read()
plt.imshow(frame[:,:,::-1])