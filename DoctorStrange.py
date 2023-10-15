import math
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.5, maxHands=2)  # Ajusta la confianza de detección según sea necesario

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
shield = cv2.VideoCapture("shield.mp4")

def mapFromTo(x, a, b, c, d):
    return (x - a) / (b - a) * (d - c) + c

def Overlay(background, overlay, x, y, size):
    background_h, background_w, c = background.shape
    imgScale = mapFromTo(size, 200, 20, 1.5, 0.2)
    overlay = cv2.resize(overlay, (0, 0), fx=imgScale, fy=imgScale)
    h, w, c = overlay.shape
    try:
        if x + w / 2 >= background_w or y + h / 2 >= background_h or x - w / 2 <= 0 or y - h / 2 <= 0:
            return background
        else:
            overlayImage = overlay[..., :3]
            mask = overlay / 255.0
            background[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)] = (1 - mask) * background[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)] + overlay
            return background
    except:
        return background

showShield = True
changeTimer = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)  # Cambiado para obtener una imagen con las manos dibujadas
    final = img
    if hands:
        success, shieldImage = shield.read()
        if not success:
            shield.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, shieldImage = shield.read()

        for hand in hands:
            bbox = hand["bbox"]
            handSize = bbox[2]
            cx, cy = hand["center"]
            if 1 in detector.fingersUp(hand):
                final = Overlay(final, shieldImage, cx, cy, handSize)

    cv2.imshow("Doctor Strange", cv2.flip(final, 1))
    cv2.waitKey(1)
