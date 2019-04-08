# Created By Antonios Kritsas
# Importing Opencv & Numpy
import numpy as np
import cv2



# Initiate the Cameras Feed
camera = cv2.VideoCapture(0)

while True:
    # Reading the camera frames
    _, frame = camera.read()
    # Blurring the frame
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Finding the contours
    _, contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ret, thresh = cv2.threshold(hsv, 127, 255, 0)

    for contour in contours:
        df = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(df, mask, 1, (0, 255, 0), 3)


    # Calling to display the two pictures in order to find the countoures
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # Defining the Exit Key
    exitKey = cv2.waitKey(0)
    if exitKey == 27:
        break


camera.release()
cv2.destroyAllWindows()