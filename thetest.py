## Making all the files together
import numpy as np
import cv2
import glob

def ocr():
    image = 'identify.png'
    template_data = []
    # make a list of all template images from a directory
    files1 = glob.glob('cards\\*.png')

    for myfile in files1:
        image = cv2.imread(myfile, 0)
        template_data.append(image)

    test_image = cv2.imread('identify.png')
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    # loop for matching
    for tmp in template_data:
        (tH, tW) = tmp.shape[:2]
        cv2.imshow("Template", tmp)
        cv2.waitKey(100)
        cv2.destroyAllWindows()
        result = cv2.matchTemplate(test_image, tmp, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + tW, top_left[1] + tH)
        cv2.rectangle(test_image, top_left, bottom_right, 255, 2)

    cv2.imshow('Result', test_image)
    cv2.waitKey(0)




cap = cv2.VideoCapture(0)


# While this is Valid Read the data from camera
while True:
    _, frame  = cap.read()
    # Bluring the frame of the web cam
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    # Grayscale the Income Blue Frame
    convertedColor = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # Adding threshold for Black Text
    img, mask = cv2.threshold(convertedColor, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(convertedColor, convertedColor, mask=mask)
    # Finding the contours inside the Live Feed
    contours = cv2.findContours(image_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # Printing contours to see if the data match my logic
    idx = 0
    # Looping inside the contours array
    for c in contours:
        area = cv2.contourArea(c)


        if area > 5000:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.07 * peri, True)
            cv2.drawContours(frame, [approx], -1, (255, 0, 255), 2)
            x, y, w, h = cv2.boundingRect(c)
                if w > 50 and h > 50:
                    new_img = frame[y:y + h, x:x + w]
                    cv2.imwrite('identify.png', new_img)
                cv2.imshow('frame', frame)


            key = cv2.waitKey(1)
            if key == 27:
                break

cap.release()
cv2.destroyAllWindows()





if __name__ == "__main__":
    thTEst()
    # ocr()