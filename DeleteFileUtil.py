#!/usr/bin/python3

import os
import re
from sys import argv
import logging
import logging.config

class DeleteFileUtil:
    
    def __init__(self, dirname, sizestr):
        self.dirname = dirname
        self.sizestr = sizestr
        logging.config.fileConfig('motionSenseLog.conf',disable_existing_loggers=0)
        self.logger = logging.getLogger('motionSenseLogger')

    def file_size(self):
        nums = re.findall('^\d+', self.sizestr)
        if len(nums) != 1:
            raise ValueError("incorrect size format, number not found in the beginning: " + self.sizestr)
        size = nums[0]
        suffix = self.sizestr[len(size):]
        degree = 0
        if suffix == "K":
            degree = 1
        elif suffix == "M":
            degree = 2
        elif suffix == "G":
            degree = 3
        elif suffix == "T":
            degree = 4
        elif suffix != "":
            raise ValueError("unknown suffix: " + suffix)
        size = int(size) * (1024 ** degree)
        return size

    def get_files_with_size(self):
        filepaths = filter(os.path.isfile, [os.path.join(self.dirname, basename) for basename in os.listdir(self.dirname)])
        filepaths = [(filepath, os.path.getsize(filepath)) for filepath in filepaths]
        filepaths.sort(key=lambda filepath: os.path.getmtime(filepath[0]))
        return filepaths

    def deleteFilesUntilDirectorySize(self):
        max_size = self.file_size()
        files = self.get_files_with_size()    
        current_size = sum([filep[1] for filep in files])
        i = 0
        while current_size > max_size:
            filep = files[i]
            self.logger.info("removing " + filep[0])
            os.remove(filep[0])
            current_size -= filep[1]
            i += 1


# deleteFileUtil = DeleteFileUtil('/home/pi/workspace/picamera/uploads', '10M')
# fileSize = deleteFileUtil.file_size()
# print(fileSize)
# files = deleteFileUtil.get_files_with_size()
# for filep in files:
#     print (filep)
# deleteFileUtil.deleteFilesUntilDirectorySize()


