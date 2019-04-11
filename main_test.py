import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
	# Capture frame-by-frame
	_, frame = cap.read()
	blur = cv2.GaussianBlur(frame, (5, 5), 0)
	# Our operations on the frame come here
	gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	th2 = cv2.adaptiveThreshold(gray, 100, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

	# _, thresh_img = cv2.adaptiveThreshold(gray, 80, 50, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


	contours = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
	print(contours)

	for c in contours:
		area = cv2.contourArea(c)
		if area > 5000:
			cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
			cv2.imshow('frame', frame)
			# cv2.imshow("thresh", thresh_img)
	if cv2.waitKey(1)  == 27:
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()