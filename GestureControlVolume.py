import cv2
import time 
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import comtypes

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
# print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")


while True:
  success, img = cap.read()
  img = cv2.flip(img, 1)
  img = detector.findHands(img)
  lmList = detector.findPosition(img, draw=False)
  if len(lmList) != 0:
    # print(lmList[4], lmList[8])
      
    x1, y1 = lmList[4][1], lmList[4][2] 
    x2, y2 = lmList[8][1], lmList[8][2] 
    
    cx, cy = (x1+x2)//2, (y1+y2)//2
      
    cv2.circle(img, (x1, y1), 10, (0, 255, 255), cv2.FILLED)
    cv2.circle(img, (x2, y2), 10, (0, 255, 255), cv2.FILLED)
    
    cv2.line(img, (x1, y1),(x2, y2), (0, 255, 255), 3)

    cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
    
    length = math.hypot(x2-x1, y2-y1)
    # print(length)
    
    vol = np.interp(length, [20, 140], [minVol, maxVol])
    print(int(length), vol)
    
    volume.SetMasterVolumeLevel(vol, None)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 2)

    volBar = np.interp(length, [20, 140], [400, 150])
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    volPerc = np.interp(length, [20, 140], [0, 100])
    cv2.putText(img, f'{int(volPerc)} %', (40, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    
    if length < 50:
      cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
  
  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime  
  
  cv2.putText(img, f'FPS: {int(fps)}',(40, 70), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 255, 255), 2)
  cv2.imshow("Image:", img)
  cv2.waitKey(1)