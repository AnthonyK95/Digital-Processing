# Is working not tested with card

import numpy as np
import cv2


cap = cv2.VideoCapture(0)


while True:

    _, frame  = cap.read()
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # lower = np.array([38, 86, 0])
    # upper = np.array([121, 255, 255])
    # mask = cv2.inRange(hsv, lower, upper)

    ret, mask = cv2.threshold(hsv, 180, 255, cv2.THRESH_BINARY_INV)
    # mask.astype('int')
    image_final = cv2.bitwise_and(hsv, hsv, mask=mask)

    # Adding threshold for black text
    # _, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(new_img, kernel, iterations=9)
    contours = cv2.findContours(image_final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    print(contours)
    for c in contours:
        area = cv2.contourArea(c)

        if area >= 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()