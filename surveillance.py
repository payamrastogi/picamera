#!/usr/bin/env python
from datetime import datetime, time
from picamera import PiCamera, Color
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os

def getCameraInstance():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.brightness = 50
    return camera

def capture(camera):
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
        upload(drive)
        sleep(sleepTime)
    camera.stop_preview()


def getDriveInstance():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)
    return drive

def upload(drive):
    os.chdir("/home/pi/upload")
    for file in glob.glob("*.jpg"):
        print (file)
        with open(file, "r") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({ 'title': fn })
            file_drive.SetContentFile(fn)
            file_drive.Upload()
            print ("The file: " + fn + " has been uploaded ")
            os.remove(fn)

if __name__ == '__main__':
    drive = getDriveInstance()
    camera = getCameraInstance()
    capture(camera)
