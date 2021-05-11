import numpy as np
import cv2
import serial
import math
import time

# initialization
ser = serial.Serial('COM6',9600)
ex = 0
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
tp = 300
ty = 315

# Main loop
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,165,255),2)
        ty = x + math.floor(w/2)
        tp = y + math.floor((7*h) / 20)

    # Converting coordinates to pitch and yaw angles for servos
    sendy = str(math.floor(ty*(-45/573)+117.9))
    sendp = str(math.floor(tp*(-45/470)+75))


    # ensures that sendy is 3 butes
    if len(sendy) == 2 :
        sendy = '0' + sendy
    elif len(sendy) == 1:
        sendy = '00' + sendy
    elif len(sendy) < 1 or len(sendy) > 3 :
        sendy = '000'
    else :
        sendy = sendy

    if len(sendp) == 2 :
        sendp = '0' + sendp
    elif len(sendy) == 1:
        sendp = '00' + sendp
    elif len(sendp) < 1 or len(sendp) > 3 :
        sendp = '000'
    else :
        sendp = sendp



    #pitch and yaw positions ready to be sent
    send = sendp + sendy
    #print(sendy)
    ser.write(send.encode('utf-8'))
    time.sleep(.001)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
