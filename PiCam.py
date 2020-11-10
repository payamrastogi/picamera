#!/usr/bin/env python
from datetime import datetime, time
from picamera import PiCamera, Color
from time import sleep
import logging
import logging.config

class PiCam:
    
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15
        self.camera.brightness = 50
        self.camera.annotate_foreground = Color('yellow')
        self.sleepTime = 30
        logging.config.fileConfig('piCamLog.conf',disable_existing_loggers=0)
        self.logger = logging.getLogger('picamlogger')
    
    def capture(self):
        fileName = ''
        try:
            self.camera.start_preview()
            
            if self.isDark():
                self.camera.brightness = 55
                self.sleepTime = 30
            else:
                self.camera.brightness = 50
                self.sleepTime = 30
            
            sleep(self.sleepTime)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            self.camera.annotate_text = dt_string
            fileName = '/home/pi/upload/picam-{}.jpg'.format(now)
            self.camera.capture(fileName)
            self.logger.info("Captured:"+fileName)
            self.camera.stop_preview()
        except Exception as e:
            self.logger.error("Exception occurred", exc_info=True)
        return fileName
    
    def isDark(self):
        now = datetime.now()
        nowTime = now.time()
        if nowTime >= time(18,00) or nowTime <= time(7,00):
            return True
        return False

#piCam = PiCam()
#fileName = piCam.capture()
#print(fileName)