import cv2
from src.camera import *

camera = Camera(True)
while (True):
    camera.turn_on()
    camera.update_values()
    k = cv2.waitKey(10)
    print k
    if k == 1048603:  # Esc key breaks out of program
        exit()
    elif k== 1048586:
        print 'Enter Key Pressed:'


