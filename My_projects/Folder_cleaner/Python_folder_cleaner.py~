from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):    #.listdir() returns list of files in same directionary
            file_type = filename.split(".")[-1]         #this returns a non string of the file extension
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            if str(file_type) == "py":                          #new destination depends on file type
                new_destination = py_folder + "/" + filename
            os.rename(src, new_destination)

''' TO DO:
get this so that the downloads folder checks what type of file it is and moves it into correct folder
'''

folder_to_track = "/home/nathancrowley/test_track_folder"            #what folder auto takes in files
folder_destination = "/home/nathancrowley/test_destination_folder"   #where they go
py_folder = "/home/nathancrowley/test_py_folder"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

