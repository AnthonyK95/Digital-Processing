# Created By Antonios Kritsas
import numpy as np
import cv2


def getRectangle():
    # Importing the image into the function
    img = cv2.imread(file_name)

    # Clone the image
    img_final = cv2.imread(file_name)

    # Making the image gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Adding threshold to the image by setting it to binary
    ret, mask = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)

    image_final = cv2.bitwise_and(img_gray, img_gray, mask=mask)
    # Adding threshold for black text
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)

    # Calculating the orientation of the squares
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(new_img, kernel, iterations=9)

    # Getting Contours
    contours, hierachy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index = 0
    for contour in contours:

        # Get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        # cv2.resizeWindow('Image', 600, 600)
      #  cropped = img_final[y:y + h, x: x + w]

      #  s = file_name + '/' + str(index) + '.jpg'
        # cv2.imwrite(s, cropped)
        # index = index + 1


    cv2.imshow('Contour', img)
    cv2.waitKey()










cv2.destroyAllWindows()
# Importing the 22.PNG as variable
file_name = 'cards/22.png'
# Starting the sequence
getRectangle()