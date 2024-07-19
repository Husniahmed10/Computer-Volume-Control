import time
import numpy as np
import cv2 as cv
import Hand_Tracking_Module as htm
import math
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


wCam, hCam = 640, 480

cap = cv.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector()


devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw = False)
    
    if len(lmlist) != 0:
        
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        
        
        cv.circle(img, (x1, y1), 10, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 10, (255, 0, 255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        
        length = math.hypot(x2 - x1, y2 - y1)
        print(length)
        
        if length < 20:
            cv.circle(img, (x1, y1), 10, (0, 255, 0), cv.FILLED)
            cv.circle(img, (x2, y2), 10, (0, 255, 0), cv.FILLED)
        
        vol = np.interp(length, [5, 105], [minVol, maxVol])
        volBar = np.interp(length, [5, 105], [400, 150])
        volPer = np.interp(length, [5, 105], [0, 100])
        
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)
        
    cv.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 0, 0), cv.FILLED)
    cv.putText(img, f'{int(volPer)} %', (40, 450), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)        
        
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, f'FPS: {int(fps)}', (40, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    
    cv.imshow("Image", img)
    cv.waitKey(1)