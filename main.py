
import pyautogui
import statistics
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
xLocations = []
yLocations = []

pyautogui.FAILSAFE = False
KEY_INPUT = False
KEY = ''

cap = cv2.VideoCapture(0)

def setInput(key):
    KEY = key
    KEY_INPUT = True

def clearInput():
    KEY_INPUT = False

def stabilize(xLocations, yLocations):
    if len(xLocations) > 5:
        xLocations.pop(0)
    if len(yLocations) > 5:
        yLocations.pop(0)

    return int(round(statistics.median(xLocations))), int(round(statistics.median(yLocations)))
    

def detectIris(eye, circles):
    closestIndex = 0
    curSum = 0 
    lowestSum = sys.maxint
    for i, j in enumerate(circles):
        for k in range(j[0][0], j[0][0] + 2 * j[0][2]):
            for m in range(j[0][1], j[0][1] + 2 * j[0][2]):
                if k > len(eye) - 1:
                    k = len(eye) - 1
                if m > len(eye[k]) - 1:
                    m = len(eye[k]) - 1
                curSum += eye[k][m]
        
        if curSum <= lowestSum:
            lowestSum = curSum
            closestIndex = i

        curSum = 0

    return circles[closestIndex][0]

def getLeftEye(eyes):
    if len(eyes) == 1:
        return eyes[0]
    if int(eyes[0][0]) <= int(eyes[1][0]):
        return eyes[0]
    return eyes[1]            
    

    if leftmostIndex > len(eyes) - 1:
        return eyes[len(eyes) - 1]
    elif leftmostIndex < 0:
        return [0, 0, 0, 0]
    else:
        return eyes[leftmostIndex]

def display(): 
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if KEY_INPUT:
            if keyboard.is_pressed(KEY):
                pyautogui.click()

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
        
            if len(eyes) > 0 and len(eyes[0]) > 0:
                leftEye = getLeftEye(eyes)
                leftEyeImg = img[leftEye[1]+y:leftEye[1]+y+leftEye[3], leftEye[0]+x:leftEye[0]+x+leftEye[2]]
                if leftEye[2] > 0 and leftEye[3] > 0:
                    cv2.imshow("cropped", leftEyeImg)
                    leftEyeGray = cv2.cvtColor(leftEyeImg, cv2.COLOR_BGR2GRAY)

                    cv2.rectangle(roi_color, (leftEye[0],leftEye[1]), (leftEye[0]+leftEye[2], leftEye[1]+leftEye[3]), (0, 255, 0), 2)
                    circles = cv2.HoughCircles(leftEyeGray,cv2.HOUGH_GRADIENT,1, 20, param1=30, param2=15, minRadius=0, maxRadius=0)
                    print(circles)
                    if isinstance(circles, (list, tuple, np.ndarray)):
                        circles = np.uint16(np.around(circles))
                        curCircle = detectIris(leftEyeGray, circles)
                        xLocations.append(curCircle[0] + leftEye[0] + x)
                        yLocations.append(curCircle[1] +  leftEye[1] + y)
                        curX, curY = stabilize(xLocations, yLocations)
                        cv2.circle(img,(curX, curY),leftEye[2],(0,255,0),2)
                        cv2.circle(img,(curX, curY),2,(0,0,255),3)
                        mouseX, mouseY = pyautogui.position()
                        if curX + x - mouseX >= 5 or curY + y - mouseY >= 5:
                            pyautogui.moveRel((curX + x - mouseX) * 1.5, (curY + y - mouseY) * 1.5)

        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

