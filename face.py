import numpy
import cv2 

face_cascade = cv2.CascadeClassifier(r'C:\Users\\root\AppData\Local\Programs\Python\Python39\Lib\site-packages\cv2\data\haarcascade_frontface.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()