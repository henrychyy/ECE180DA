import cv2


cam = cv2.VideoCapture(0)
rval, frame = cam.read()
cv2.imwrite('yy.jpeg', frame)
print("yes")
