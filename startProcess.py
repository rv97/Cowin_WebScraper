from cowin_parser import CowinParser
import threading
from notify_run import Notify
import sys
import os

notify = Notify()

def registerNotification():
    result = str(notify.register())
    return result.splitlines()[1]

def sendNotification():
    file = open("hospitaldata.txt", "r")
    data = []
    if file:
        data.append(file.read())
        file.close()
    notify.send(str(data))

def runSearch(searchDetails):
    cowinParser = CowinParser()
    cowinParser.startSearch(searchDetails)
    sendNotification()
    print("Notification Sent")
    os.remove("hospitaldata.txt")
    sys.exit()

def startThread(searchDetails):
    thread = threading.Thread(target=runSearch, args=(searchDetails, ))
    thread.start()
