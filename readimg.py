import time 


import pytesseract 
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import os 
import io
import cv2
from threading import Thread
from PIL import Image
import pyttsx3
engine = pyttsx3.init()

# thread function to convert string to audio 
def txt_audio(msg):
    print('audio begin')
    s = msg
    engine.say(s)
    engine.runAndWait()

# function to convert image to text 
def img_txt(image):
    content = pytesseract.image_to_string(image)
    print('audio begin')
    s = content
    engine.say(s)
    engine.runAndWait()
    print(content)


# Open the camera
camera = cv2.VideoCapture(0)

# Allow camera to warm up
time.sleep(2)

# Capture the image
ret, frame = camera.read()

# Release the camera
camera.release()

# Save the captured image to a file
cv2.imwrite("captured_image.jpg", frame)

# Read the captured image using cv2.imread
captured_image = cv2.imread("captured_image.jpg")


# Convert the resized image to text
img_txt(captured_image)


