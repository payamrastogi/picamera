#!/usr/bin/env python
from datetime import datetime, time
from picamera import PiCamera, Color
from time import sleep

def getCameraInstance():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.brightness = 50
    return camera

def capture(camera):
    camera.start_preview()
    for i in range(1):
        sleep(5)
        now = datetime.now()
        nowTime = now.time()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        camera.brightness = 50
        if nowTime >= time(18,00) or nowTime <= time(7,00):
            camera.brightness = 55
        camera.annotate_foreground = Color('yellow')
        camera.annotate_text = dt_string
        camera.capture('/home/pi/upload/picam-%s.jpg' %now)
    camera.stop_preview()

if __name__ == '__main__':
    camera = getCameraInstance()
    capture(camera)