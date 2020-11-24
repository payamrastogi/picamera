#!/bin/sh
file="/home/pi/workspace/picamera/motionSense.pid"
if [ -f $file ] ; then
    kill -9 `cat $file`;
    rm $file;
fi
if pgrep MotionSense.py; then 
    pkill MotionSense.py; 
fi