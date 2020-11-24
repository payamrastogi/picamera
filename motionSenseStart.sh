#!/bin/bash
file="/home/pi/workspace/picamera/motionSense.pid"
rm -f $file;
cd /home/pi/workspace/picamera
source venv/bin/activate
nohup python3 MotionSense.py > nohup.out 2>&1 &
echo $! > $file