#!/bin/sh
if pgrep Surveillance.py; then 
    pkill Surveillance.py; 
fi
file="/home/pi/camera/picam.pid"
rm -f $file;
nohup python Surveillance.py > nohup.out 2>&1 &
echo $! > $file