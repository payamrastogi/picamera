#!/bin/sh
if pgrep Surveillance.py; then 
    pkill Surveillance.py; 
fi
file="/home/pi/workspace/picamera/picam.pid"
rm -f $file;
nohup python Surveillance.py > nohup.out 2>&1 &
echo $! > $file