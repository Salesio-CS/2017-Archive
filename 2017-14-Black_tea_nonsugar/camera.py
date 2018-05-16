#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time

cap = cv2.VideoCapture(0)
while(True):
    r, frame = cap.read()
    cv2.imshow(`camera captuer`, frame)

    k = cv2.waitKey(500)
    if(k == 27):
        break
cap.release()
cv2.destroyAllWindows()
