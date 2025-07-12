from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import datetime
import csv

class myHandler(FileSystemEventHandler):

    def on_modified(self, event):
        log(datetime.datetime.now(), event.event_type , event.src_path)
        
    def on_created(self, event):
        log(datetime.datetime.now(), event.event_type , event.src_path)
        
    def on_deleted(self, event):
        log(datetime.datetime.now(), event.event_type , event.src_path)
        
    def on_moved(self, event):
        log(datetime.datetime.now(), event.event_type , event.src_path)


def main():
    location = input('Which Directory Would You Like To Monitor?\nType . For Current Directory:\n')

    observer = Observer()
    observer.schedule(myHandler(), location, recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()



def log(time, action, directory):
    with open('./logger/logger.csv', 'a', newline = '') as csvFile:
        file = csv.writer(csvFile, delimiter='\t')

        new_time = time.replace(microsecond=0)
        new_directory = directory[2:]

        file.writerow([new_directory, action.upper(), new_time])


if __name__ == '__main__':
    main()