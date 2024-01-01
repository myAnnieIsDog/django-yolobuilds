# Standard Library
import cgi
import datetime as dt
import math
import os
import random
import re
import pickle
import socket
import sys
import time
import urllib

# pip modules
from pprint import pprint 

# User modules
from process_timer import Log_start, Log_end


def main():
    modOS()


def standardLibrary():
    print(help('modules'))


def modOS():
    print("Working with the 'os' module\n")   
    print(os.getcwd())

    path = "G:\My Drive\Yolo Builds"
    path2 = "Python Testing/nested/deeper/micro"
    os.chdir(path)
    os.listdir(path)
    os.makedirs(path2)
    os.removedirs(path2)
    os.stat(path)
    dt.datetime.fromtimestamp()

    rename_directory('Inventory of Plants (1).xlsx', 'Inventory of Plants2.xlsx')
    def rename_directory(name1, name2):
        try:
            os.path.exists(name1)
            try:
                os.rename(name1, name2)
            except:
                print("File already exists.") 
        except:
            print("File not found.")

    os.walk(path)   # Tuple showing ALL folder and files in a directory.
    for dirpath, dirnames, filenames in os.walk("G:\My Drive\Yolo Builds"):
        print("\nCurrent Path:")
        pprint(dirpath)

        print("\nDirectories:")
        pprint(dirnames)

        print("\nFiles:")
        pprint(filenames)

    os.environ.get("HOME")
    os.path.join(os.environ.get("HOME"), "test.txt")
    os.path.basename(path)
    os.path.dirname(path)
    os.path.split(path)
    os.path.exists(path)
    os.path.isdir(path)
    os.path.isfile(path)
    os.path.splitext(path)  ## use this for creating backups


def listFuncs():
    pprint(dir(os))  



if __name__ == '__main__':
    log_start = Log_start()
    main()
    Log_end(log_start)
