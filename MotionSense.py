#!/usr/bin/env python
from datetime import datetime, time
from gpiozero import MotionSensor
from picamera import PiCamera
from DeleteFileUtil import DeleteFileUtil
import logging
import logging.config

class MotionSense:
    def __init__(self):
        self.camera = PiCamera()
        self.pirMotionSensor = MotionSensor(4)
        logging.config.fileConfig('motionSenseLog.conf',disable_existing_loggers=0)
        self.logger = logging.getLogger('motionSenseLogger')

    def detect(self):
        print("Called")
        fileName = ''
        self.pirMotionSensor.wait_for_motion()
        self.logger.info("Motion Detected")
        print("Motion Detected")
        if not self.isDark():
            self.camera.brightness = 50
        else:
            self.camera.brightness = 55

        now = datetime.now()
        dt_string = now.strftime("%d%m%YH%HM%MS%S")
        self.camera.annotate_text = dt_string
        fileName = '/home/pi/workspace/picamera/uploads/picam-{}.h264'.format(dt_string)
        self.camera.start_recording(fileName)
        self.pirMotionSensor.wait_for_no_motion()
        self.logger.info("Captured:"+fileName)
        self.camera.stop_recording()
        return fileName

    def isDark(self):
        now = datetime.now()
        nowTime = now.time()
        if nowTime >= time(18,00) or nowTime <= time(7,00):
            return True
        return False


motionSense = MotionSense()
deleteFileUtil = DeleteFileUtil('/home/pi/workspace/picamera/uploads', '2G')
while True:
    motionSense.detect()
    deleteFileUtil.deleteFilesUntilDirectorySize()
    
