from ObjectDetectionModule import *

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    result, objectInfo = getObjects(img,0.5,0.2,objects=['person'])
    #print(objectInfo)
    cv2.imshow("output", img)
    cv2.waitKey(1)