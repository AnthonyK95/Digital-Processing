import cv2
import numpy as np
from os import listdir

# Declaring threshold
matchingThreshold2 = 0.75
matchingThreshold1 = 0.58

# Read Shape Templates
heart = cv2.imread('cards/heart.png', 0)
spade = cv2.imread('cards/spade.png', 0)
diamond = cv2.imread('cards/diamond.png', 0)
club = cv2.imread('cards/club.png', 0)

# Read Number Templates
ace = cv2.imread('cards/ace.png', 0)
two = cv2.imread('cards/two.png', 0)
three = cv2.imread('cards/three.png', 0)
four = cv2.imread('cards/four.png', 0)
five = cv2.imread('cards/five.png', 0)
six = cv2.imread('cards/six.png', 0)
seven = cv2.imread('cards/seven.png', 0)
eight = cv2.imread('cards/eight.png', 0)
nine = cv2.imread('cards/nine.png', 0)
ten = cv2.imread('cards/ten.png', 0)
jack = cv2.imread('cards/jack.png', 0)
queen = cv2.imread('cards/queen.png', 0)
king = cv2.imread('cards/king.png', 0)




# All the mana logos are about the same size
w, h = spade.shape[::-1]
nw, nh = king.shape[::-1]

# Check &  Highlight the Result
def checkingValues(color_template, gray, check):
    results = cv2.matchTemplate(gray, color_template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(results >= matchingThreshold2)
    for pt in zip(*locations[::-1]):
        cv2.rectangle(check, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

def checkingNums(color_template, gray, check):
    results = cv2.matchTemplate(gray, color_template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(results >= matchingThreshold1)
    for pt in zip(*locations[::-1]):
        cv2.rectangle(check, pt, (pt[0] + nw, pt[1] + nh), (0, 0, 255), 2)

# Looping Through Cases
while True:
    img_to_check = cv2.imread("all.png")
    # blur1 = cv2.blur(img_to_check, (5, 5))
    blur = cv2.medianBlur(img_to_check, 5)
    # blur = cv2.GaussianBlur(img_to_check, (5, 5), 0)


    img_gray = cv2.cvtColor(img_to_check, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    checkingValues(heart, imageGray, img_to_check)
    checkingValues(spade, imageGray, img_to_check)
    checkingValues(club, imageGray, img_to_check)
    checkingValues(diamond, imageGray, img_to_check)
    checkingNums(eight, imageGray, img_to_check)







    key = cv2.waitKey(0)
    cv2.imshow("Template", img_to_check)
    if key == 27:
        break
cv2.destroyAllWindows()
