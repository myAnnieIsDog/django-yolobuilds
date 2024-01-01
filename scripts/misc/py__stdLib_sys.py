from process_timer import Log_start, Log_end
from pprint import pprint 
import os
import sys


def main():
    print("Working with the 'os' module\n")
    pprint(dir(sys))  
    print(os.getcwd())

    path = "G:\My Drive\Yolo Builds"
    path2 = "Python Testing/nested/deeper/micro"


if __name__ == '__main__':
    log_start = Log_start()
    main()
    Log_end(log_start)
