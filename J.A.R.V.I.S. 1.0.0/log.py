# log
# keeps track of all events that occur during runtime

import datetime
import os
import shutil

def log(type, message):
    with open('logs/log.txt', 'a') as f:
        now = datetime.datetime.now().time()
        f.write(f'>> ({now}) | {type} : {message}\n')

def clean_log():
    with open('logs/log.txt', 'w') as f:
        pass

def archive_log():
    now = datetime.datetime.now()
    shutil.copy('logs/log.txt', f'archived_logs/LOG: {now}.txt')

def start():
    os.makedirs('logs', exist_ok=True)
    os.makedirs('archived_logs', exist_ok=True)

    if not os.path.exists('logs/log.txt'):
        with open('logs/log.txt', 'w') as f:
            now = datetime.datetime.now()
            f.write(f'-----({now}) | LOG : NEW LOG SESSION INITIALIZED-----\n')
    else:
        with open('logs/log.txt', 'a') as f:
            now = datetime.datetime.now()
            f.write(f'-----({now}) | LOG : NEW LOG SESSION INITIALIZED-----\n')

# Example Logs
'''
log("test", "second log entry! - testing archive and clean features")
archive_log()
clean_log()
'''