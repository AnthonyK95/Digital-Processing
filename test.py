# Todo Upading with the rectangle implementation
# Wokring Progress On Recognize The Pattern Of The User

import cv2
import numpy as np

# Creating the Fake OCR
def ocr():
    print("Starting the ocr matching")


# Starting the Video Camera=> Default Value
cap = cv2.VideoCapture(0)
# While this is Valid Read the data from camera
while True:
    _, frame  = cap.read()
    # Bluring the frame of the web cam
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    # Grayscale the income blue frame
    convertedColor = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # Adding threshold to the converte
    ret, mask = cv2.threshold(convertedColor, 140, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(convertedColor, convertedColor, mask=mask)
    # Adding threshold for black text
    # , new_img = cv2.threshold(image_final, 100, 255, cv2.THRESH_BINARY)
    # Finding the contours inside the live feed
    contours = cv2.findContours(image_final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # Printing contours to see if the data match my logic
    print(contours)
    # Looping inside the contours array
    for c in contours:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 255), 2)
            cv2.imshow('frame', frame)

    # cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()