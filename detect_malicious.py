import os
import time
import pyudev
import glob
import hashlib

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if fullPath[-3:] == '.py':
                allFiles.append(fullPath)
    return allFiles

def generate_hashes(path, hashed_list):
    for file in getListOfFiles(path):
        f = open(file, "r")
        m = hashlib.sha1(f.read().encode()).hexdigest()
        hashed_list.append(m)
    hashed_list = list(dict.fromkeys(hashed_list))    
        
def match_hashes(malicious_hashed_path, hashed_list, fullPath, output):
    mal_list = []
    file = open(malicious_hashed_path, "r")
    lines = file.readlines()
    for line in lines:
        mal_list.append(line)
    for digest in hashed_list:
        digest = digest + '\n'
        if digest in mal_list:
            output.append(fullPath + " ==>> MALICIOUS CODE FOUND!")
            return
    output.append(fullPath + " ==>> USB is safe!")

def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    output = []

    for device in iter(monitor.poll, None):
        if device.action == 'add':
            # ACTIONS
            time.sleep(7)
            for folder in os.listdir("/media/abdullah/"):
                hashed_list = []
                fullPath = os.path.join("/media/abdullah/", folder)
                if os.path.isdir(fullPath):
                    generate_hashes(fullPath, hashed_list)
                    match_hashes("digests.txt", hashed_list, fullPath, output)
        break
    output = list(dict.fromkeys(output))
    for o in output:
        print(o)
        
if __name__ == "__main__":
    main()

