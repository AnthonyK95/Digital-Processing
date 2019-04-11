# Backup File
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
    ret, mask = cv2.threshold(convertedColor, 180, 255, cv2.THRESH_BINARY_INV)
    image_final = cv2.bitwise_and(convertedColor, convertedColor, mask=mask)
    # Adding threshold for black text
    _, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(new_img, kernel, iterations=9)
    contours = cv2.findContours(image_final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    print(contours)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            cv2.imshow('frame', frame)
            # After the showing start the OCR matching
            ocr()

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()