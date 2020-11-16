#!/bin/sh
file="/home/pi/workspace/picamera/picam.pid"
if [ -f $file ] ; then
    kill -9 `cat $file`;
    rm $file;
fi
if pgrep Surveillance.py; then 
    pkill Surveillance.py; 
fi