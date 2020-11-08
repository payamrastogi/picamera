#!/usr/bin/env python
from datetime import datetime, time
from picamera import PiCamera, Color
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os
import logging
import logging.handlers
import logging.config

logging.config.fileConfig('log.conf',disable_existing_loggers=0)
logger = logging.getLogger('picamlogger')

def getCameraInstance():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.brightness = 50
    return camera

def capture(camera):
    try:
        camera.start_preview()
        while(True):
            now = datetime.now()
            nowTime = now.time()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            camera.brightness = 50
            sleepTime = 30
            if nowTime >= time(18,00) or nowTime <= time(7,00):
                camera.brightness = 55
                sleepTime = 120
            camera.annotate_foreground = Color('yellow')
            camera.annotate_text = dt_string
            camera.capture('/home/pi/upload/picam-%s.jpg' %now)
            logger.info('captured /home/pi/upload/picam-%s.jpg', now)
            upload(drive)
            sleep(sleepTime)
        camera.stop_preview()
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)


def getDriveInstance():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)
    return drive

def upload(drive):
    try:
        os.chdir("/home/pi/upload")
        for file in glob.glob("*.jpg"):
            logger.info('%s', file)
            with open(file, "r") as f:
                fn = os.path.basename(f.name)
                file_drive = drive.CreateFile({ 'title': fn })
                file_drive.SetContentFile(fn)
                file_drive.Upload()
                logger.info("The file %s has been uploaded", fn)
                os.remove(fn)
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)

if __name__ == '__main__':
    drive = getDriveInstance()
    camera = getCameraInstance()
    capture(camera)
