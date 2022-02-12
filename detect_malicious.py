import os
import time
from numpy import delete
import pyudev
import glob
import hashlib
import requests

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

def generate_hashes(path, hashed_list,Py_files_pathes):
    for file in getListOfFiles(path):
        f = open(file, "r")
        m = hashlib.sha1(f.read().encode()).hexdigest()
        hashed_list.append(m)
        Py_files_pathes.append(file)
    hashed_list = list(dict.fromkeys(hashed_list))    
        
def match_hashes(mal_list, hashed_list, fullPath, output, Py_files_pathes, Sus_files_list, sus_hashes):
    for digest in hashed_list:
        if digest in mal_list:
            sus_hashes.append(digest)
            Sus_files_list.append(Py_files_pathes[hashed_list.index(digest)])


def Delete_mal(Files):
    for i in Files:
        os.remove(i)
        print('{} is deleted successfully'.format(i))
    print("All malicious files were removed")

def WhiteList(hashes):
    URL = ""
    Files= {}
    for i in hashes:
        Files ['hash {}'.format(hashes.index(i)+1)] = i
    r = requests.post(URL,Files)
    print(r)
# def Ignore():
#     #to do

# def Detection():
#     context = pyudev.Context()
#     monitor = pyudev.Monitor.from_netlink(context)
#     monitor.filter_by(subsystem='usb')
#     output = []
#     print("Please enter the USB device")
#     for device in iter(monitor.poll, None):

#         if device.action == 'add':
#             # ACTIONS
#             time.sleep(7)
#             for folder in os.listdir("/media/abdullah/"):
#                 hashed_list = []
#                 Sus_files_list = []
#                 Py_files_pathes=[]
#                 Sus_hashes = []
#                 fullPath = os.path.join("/media/abdullah/", folder)
#                 if os.path.isdir(fullPath):
#                     generate_hashes(fullPath, hashed_list,Py_files_pathes)
#                     match_hashes("digests.txt", hashed_list, fullPath, output,Py_files_pathes,Sus_files_list,Sus_hashes)
#         break
#     output = list(dict.fromkeys(output))
#     for o in output:
#         print(o)
#         if len(Sus_files_list) !=0:
#             print("the following files are suspected to be malicious")
#             for i in Sus_files_list:
#                 print(i)
#             #make the user delete the files OR IGNORE the files (white list) OR suspend the USB
#             UserInput = input("enter\n1 for deleting \n2 for white listing the file\n3 for suspending the USB\n")
#             if UserInput == '1':
#                 Delete(Sus_files_list)
#             elif UserInput == '2':
#                 WhiteList(Sus_hashes)
#             elif UserInput == '3':
#                 os.system('sudo eject /media/abdullah/USB\ stick')

def main():
        Detection()
if __name__ == "__main__":
    main()

