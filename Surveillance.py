from threading import Thread, Lock
import time
import random
from Queue import Queue
from PiCam import PiCam
from PyDrive import PyDrive

queue = Queue()

class ProducerThread(Thread):
    def run(self):
        piCam = PiCam()
        global queue
        while True:
            fileName = piCam.capture()
            queue.put(fileName)
            print ("produced", fileName)

class ConsumerThread(Thread):
    def run(self):
        pyDrive = PyDrive()
        global queue
        while True:
            fileName = queue.get()
            pyDrive.upload(fileName)
            queue.task_done()
            print ("consumed", fileName)
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
