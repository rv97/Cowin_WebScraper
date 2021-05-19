from cowin_parser import CowinParser
import threading
from notify_run import Notify
import os
import time
import sys

notify = Notify()

def registerNotification():
    result = str(notify.register())
    print("Notification Registered Successfully")
    return result.splitlines()[1]

def sendNotification():
    file = open("hospitaldata.txt", "r")
    data = []
    if file:
        data.append(file.readlines())
        file.close()
    notify.send(str(data))

def runSearch(searchDetails):
    cowinParser = CowinParser()
    while True:  
        cowinParser.startSearch(searchDetails)
        sendNotification()
        print("Notification Sent")
        os.remove("hospitaldata.txt")
        time.sleep(300)

def startThread(searchDetails):
    thread = threading.Thread(target=runSearch, args=(searchDetails, ))
    thread.start()
