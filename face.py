import numpy
import cv2 

face_cascade = cv2.CascadeClassifier(r'C:\Users\\root\AppData\Local\Programs\Python\Python39\Lib\site-packages\cv2\data\haarcascade_frontface.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    #faces = face_cascade.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in face_cascade:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h]

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
