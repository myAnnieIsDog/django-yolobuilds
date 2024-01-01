"""Standard Library Modules
https://docs.python.org/3/py-modindex.html
"""

def main():
    # test_argparse()
    # test_array()
    # test_atexit()
    # test_bisect()
    # test_bz2()
    # test_calendar(2023)
    # test_collections()
    # test_colorsys()
    # test_csv()
    # test_dataclasses()
    # test_datetime()
    # test_decimal()
    # test_fractions()
    # test_getpass()
    # test_graphlib()
    # test_gzip()
    # test_math()
    # test_os()
    test_pathlib()
    # test_json()
    # test_keyword()


    # test_lzma()
    # test_wave() # Need to learn this one.
    # test_webbrowswer()
    # test_zipfile() # Need to learn more about all the zip modules.




    # test_txt()
def test_txt():
    data = """\
        Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
        nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
        sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
        pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
        Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
        felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
        dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
    with open("test.txt", "w") as f:
        f.write(data)

    with open("test.txt", "r") as f:
        content = f.read(data)
    print(content)


# import __future__
# import __main__       # imports namespace of the top-level module.
# import __thread__
# import abc
import argparse
def test_argparse():
    parser = argparse.ArgumentParser(
        prog="modules",
        description="Test the argparse standard library module.",
        epilog="Text at the bottom of help.")
    parser.add_argument("filename", default="test.txt")
    parser.add_argument("-c", "--count")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)
# parse() # This function was never operable. I need to learn argparse.


import array        # a `list` with a specified data type
def test_array():
    print(array.typecodes)
    ray = array.array("i", (1,2,3))

    ray.append(5)
    ray.extend([1,2,3,4,5,6,7,8,9,0])
    ray.fromlist([12,13,14,15])
    print("5 is in the list", ray.count(5), "times.")

    index = ray.index(5)
    index2 = ray.index(5, index + 1)
    print("5 occurs at indexes", index, "and", index2)

    ray.insert(2, 5)
    ray.pop(-1)
    ray.remove(7)
    print(ray)

    ray.reverse()
    print(ray)

    listed = ray.tolist()
    print(listed)


# import ast
# import asynchio
import atexit
@atexit.register # registering by decorator only works if there are no arguments.
def test_atexit():
    print("So long, and thanks for all the fish.")
# atexit.unregister(test_atexit)
# atexit.register(test_atexit) # use this method if the function has arguments
# atexit.register(test_atexit) # second registration results in duplicate output.


# import base64     # not the same as uu
# import bdb        # debugger
# import binascii   # see uu and base64
import bisect
def test_bisect():
    testList = ["a", "b", "c", "e", "f", "g"]
    testList.insert(bisect.bisect_left(testList, "d"),"d")
    bisect.insort(testList, "e")
    print(testList)


# import builtins   # for wrapping a built-in function
import bz2
def test_bz2():
    data = b"""\
    Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
    nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
    sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
    pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
    Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
    felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
    dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""

    c = bz2.compress(data)
    print("bz2 Compression Ratio:", len(data) / len(c))  # Data compression ratio

    d = bz2.decompress(c)
    print("Pre-Compression = Post-Decompression:", data == d)  # Check equality to original object after round-trip


import calendar     # see also datetime and time modules.
from calendar import setfirstweekday, prcal, prmonth, isleap, leapdays, monthrange, weekday
from calendar import day_name, month_name, day_abbr, month_abbr     # <-- attributes

def test_calendar(year):
    setfirstweekday(6) # sets Sunday as day 0
    prcal(year, m=3) 
    prmonth(year,10)
    print(year, "is a leap year.") if isleap(year) else print(year, "is not a leap year.")
    print("There are", leapdays(2000, 2100), "leap days between 2000 and 2100.")
    print("Oct range:", monthrange(year, 10))
    print("Halloween is:", day_abbr[weekday(year, 10, 31)+1]) # Uses Mon = 0. Adjust accordingly.

    htmlCal = calendar.HTMLCalendar(firstweekday=0)
    # print(htmlCal.formatmonth(year, 10, withyear=True))
    # print(htmlCal.formatyear(year, width=3))       


# import cmath      
# import cmd
# import codes
# import codecs
# import codeop
import collections
def test_collections():
    # Built-in Containers:
    a_tuple = ("A", "B", "C", "D")
    a_list = [1, 2, 3, 4, 5]
    a_set = {"a", "d", "b", "c", "e"}
    a_dict = {"A Tuple": a_tuple, "A List": a_list, "A Set": a_set}
    print("A dictionary containing a tuple, a list, and a set:")
    for k, v in a_dict.items():
        print(k, ":", v)

    # Collections containers:
    a_ChainMap = collections.ChainMap(a_dict)
    print("Maps:", a_ChainMap.maps)
    a_ChainMap = a_ChainMap.new_child(m=a_dict)
    print("Parents:", a_ChainMap.parents)

    a_Counter = collections.Counter()
    coin_tosses = ["heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "heads", "tails", "tails", "tails", "heads", "tails"]
    
    for word in coin_tosses:
        a_Counter[word] += 1
    print(a_Counter)
    print("Total Tosses:", a_Counter.total())
    print("Eklements", *a_Counter.elements())
    print("Most Common:", a_Counter.most_common())

    round2 = ["heads", "tails", "tails"]   
    a_Counter.subtract(round2)
    print(a_Counter)
    a_Counter.update(round2)
    # Counters can be added, etc. a + b = c
    
    a_deque = collections.deque([1, 2, 3, 4, 5, 6, 7], 12)
    for _ in range(8, 25, 2):
        a_deque.append(_)
    for _ in range(30, 43, 3):
        a_deque.appendleft(_)
    print(a_deque)
    for _ in range(1, 3):
        a_deque.popleft()
    for _ in range(1, 3):
        a_deque.pop()
    a_deque.reverse()
    a_deque.rotate(5)
    print(a_deque)

    d = collections.defaultdict(list)
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for k, v in s:
        d[k].append(v)
    print(sorted(d.items()))

    # Very useful when working with csb or db tables:
    a_namedtuple = collections.namedtuple("Point", ["x", "y", "z"], defaults=[10, 0, 0])
    p = a_namedtuple(11, y=22)
    print(p)
    print(p[0]+p[1]+p[2]) # can reference position index
    print(p.x, p.y, p.z)  # or key name

    a_OrderedDict = 1
    a_UserDict = 1
    a_UserList = 1
    a_UserString = 1


import colorsys
def test_colorsys():
    h, s, v = 0.5, 0.5, 0.4
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    print("rgb=", r, g, b)
    print("hsv=", h, s, v)


# import compileall
# import concurrent
# import configparser
# import contextlib
# import contextvars
# import copy
# import copyreg
# import cProfile
import csv 

def test_csv():
    print("csv dialects:", csv.list_dialects())
    a = (
        ("left", 1),
        ("right", 2)
    )
    with open("py/some.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(a)

    filename = "py/some.csv"
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                print(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    




# import ctypes
from dataclasses import dataclass

def test_dataclasses():
    dc = InventoryItem()
    assets = dc.total_cost()
    print("   $", assets)

@dataclass #decorator examines the class to find class variables that have type annotation.
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str = "widget"
    unit_price: float = 100.00
    quantity_on_hand: int = 13

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


from datetime import datetime as dt
def test_datetime():
    now = dt.now()
    print(now.strftime("%A, %B %d, %G")) # formal
    print(now.strftime("%G-%m-%d_%H:%M:%S")) # filename suffix
    print(f"{now.date()}_{now.time()}") # filename suffix to ms
    # print(f"%a = {now.strftime("%a")} (weekday)")  
    # print(f"%A = {now.strftime("%A")} (weekday)")
    # print(f"%w = {now.strftime("%w")} (weekday)")
    # print(f"%d = {now.strftime("%d")} (day)")
    # print(f"%b = {now.strftime("%b")} (month)")
    # print(f"%B = {now.strftime("%B")} (month)")
    # print(f"%m = {now.strftime("%m")} (month 00)")
    # print(f"%y = {now.strftime("%y")} (year 00)")
    # print(f"%Y = {now.strftime("%Y")} (year 0000)")
    # print(f"%H = {now.strftime("%H")} (hour: 24:00)")
    # print(f"%I = {now.strftime("%I")} (hour: 12:00)")
    # print(f"%p = {now.strftime("%p")} (am/pm)")
    # print(f"%M = {now.strftime("%M")} (minute)")
    # print(f"%S = {now.strftime("%S")} (second)")
    # print(f"%f = {now.strftime("%f")} (ms)")
    # print(f"%z = {now.strftime("%z")} (UTC offset)")
    # print(f"%Z = {now.strftime("%Z")} (time zone name)")
    # print(f"%j = {now.strftime("%j")} (day of year)")
    # print(f"%U = {now.strftime("%U")} (week starting Sunday)")
    # print(f"%W = {now.strftime("%W")} (week starting Monday)")
    # print(f"%c = {now.strftime("%c")} (locale datetime)")
    # print(f"%x = {now.strftime("%x")} (locale date)")
    # print(f"%X = {now.strftime("%X")} (locale time)")
    # print(f"%% = {now.strftime("%%")} (literal)")

    # print(f"%G = {now.strftime("%G")} (year)")
    # print(f"%u = {now.strftime("%u")} (weekday)")
    # print(f"%V = {now.strftime("%V")} (week number)")
    # print(f"%:z = {now.strftime("%:z")} (UTC offset)")


# import dbm
import decimal
from decimal import Decimal, getcontext
def test_decimal():
    i = 1.1+2.2
    print(i, type(i))
    x = Decimal("1.1")+Decimal("2.2")
    print(x, type(x))
    



# import difflib
# import dis
# import doctest
# import email
# import enum
# import errno
# import faulthandler
# import filecmp
# import fileinput
# import fnmatch
import fractions
from fractions import Fraction
def test_fractions():
    x = Fraction(5, 2) + Fraction(1, 4)
    y = Fraction(2.5)
    z = Fraction("4/5")
    zz = z.limit_denominator(4)
    print(x, type(x))
    print(y, zz)


# import ftplib
# import functools
# import gc
# import getopt
import getpass
from getpass import getpass, getuser
def test_getpass():
    un = getuser()
    pw = getpass()
    print(un, pw)



# import gettext
# import glob
import graphlib
def test_graphlib():
    graph = {
        "Epilogue": {"End", "Beginning"}, 
        "Beginning": {"Prologue"},
        "End": {"Middle", "Beginning"}, 
        "Middle": {"Beginning"}, 
    }
    ts = graphlib.TopologicalSorter(graph)
    print(*ts.static_order())
    
    # ts.prepare()
    # while ts.is_active():
    #     for node in ts.get_ready():
    #         task_queue.put(node)
    #     node = finalized_tasks_queue.get()
    #     ts.done(node)


import gzip
def test_gzip():
    data = b"""\
    Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
    nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
    sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
    pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
    Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
    felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
    dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""

    filename = "test.gz"
    with gzip.open(filename, 'wb') as f:
        f.write(data)
    
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()
    print("File 1:", file_content)
    
    with gzip.open(filename, 'rb') as f_in, gzip.open('test2.gz', 'wb') as f_out:
        f_out.writelines(f_in)

    with gzip.open("test2.gz", 'rb') as f:
        file_content2 = f.read()
    print("File 2:", file_content2)   

    ratio = len(data) / len(gzip.compress(data))
    print("gzip ratio is ", ratio)


# import hashlib
# import heapq
# import hmac
# import html
# import http
# import idlelib
# import imaplib
# import importlib
# import inspect
import io
def test_io():
    pass

# import ipaddress
# import itertools
import json
def test_json():
    aDict = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
    }

    # Working in memory with strings
    aDictJson = json.dumps(aDict)
    aDictJsonDict = json.loads(aDictJson)
    for key, value in aDictJsonDict.items():
        print(f"   {key}:\t {value}")
    
    # Working on files

    with open("test.json", "w") as f:
        json.dump(aDict, f)
    with open("test.json", "r") as f:
        dict2 = json.load(f)
    for key, value in dict2.items():
        print(f"   {key}:\t {value}")



import keyword
def test_keyword():
    print(keyword.iskeyword("go"))


# import lib2to3
# import linecache
# import locale
# import logging
import lzma
def test_lzma():
    data = b"""\
    Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
    nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
    sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
    pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
    Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
    felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
    dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""

    filename = "test.xz"
    with lzma.open(filename, 'wb') as f:
        f.write(data)

    with lzma.open(filename, 'rb') as f:
        content = f.read()
    print(content)

    ratio = len(data) / len(lzma.compress(data))
    print("lzma ratio is ", ratio)


# import mailbox
# import marshal
import math
def test_math():
    roundUp = math.ceil(12.45)
    binomialCoeff = math.comb(12, 3)
    sign = math.copysign(1, -2)
    absoluteValue = math.fabs(-3)
    factorial = math.factorial(3)
    roundDown = math.floor(12.54)
    modula = math.fmod(13, 4)
    mantissaExp = math.frexp(12)
    invfrexp = math.ldexp(0.75, 4)
    sum = math.fsum([1,2,3,4,5,6,7])
    divisor = math.gcd(75, 125, 375)
    close = math.isclose(34.00000001, 34.0000000, rel_tol=1e-03)
    isqrt = math.isqrt(10)
    multiple = math.lcm(2,3,4,5,6,7)
    modf = math.modf(5.24)
    perm = math.perm(6, 2)
    product = math.prod([2,3,4,5,6,7])
    remainder = math.remainder(50, 4)
    sumprod = math.sumprod([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    truncated = math.trunc(3.564)

    print(roundUp, binomialCoeff, sign, absoluteValue, factorial, roundDown, modula, mantissaExp, invfrexp, sum, divisor, close)
    print(isqrt, multiple, modf, perm, product, remainder, sumprod, truncated)


    # Power and Logarithmic functions
    e = math.e
    infinity = math.inf
    squareRoot = math.sqrt(9)
    cubeRoot = math.cbrt(8)
    natLog  = math.exp(2.714) # base = e (natural log)
    log = math.log(8, 2)
    exp = math.pow(8, 1/3)

    print(squareRoot, cubeRoot, natLog, log, exp)
    
    
    # Trig
    pi = math.pi
    tau = math.tau  # 2pi
    degrees = f"{math.degrees(1.5*pi)} deg"    # radians to degrees
    radians = f"{math.radians(270)/pi}\u03C0 radians"

    sin = math.sin(0.25*pi)
    cos = math.cos(0.25*pi)
    tan = math.tan(0.25*pi)

    asin = math.asin(0.25*pi)
    acos = math.acos(0.25*pi)
    atan = math.atan(0.25*pi)
    atan2 = math.atan2(0.707, 0.707)

    euclidDist = math.dist([1,3,2], [5,3,1])  # 3D distances, etc.
    hypotenuse = math.hypot(1,3,2)

    print(degrees, radians, sin, cos, tan, asin, acos, atan, atan2)
    print(euclidDist, hypotenuse)


# import mimetypes
# import mmap
# import modulefinder
# import msivcrt
# import multiprocessing
# import netrc
# import numbers
# import operator
# import optparse
import os
def test_os():
    path = "test.txt"
    os.path.exists(path)
    os.path.isfile(path)
    os.path.isdir(path)
    
    os.path.abspath(path)  
    os.path.split(path)
    os.path.basename(path)
    os.path.dirname(path)

    accessTime = os.path.getatime(path)
    modTime = os.path.getmtime(path)
    size = os.path.getsize(path)
 
import pathlib
def test_pathlib():
    p = pathlib.Path(".")
    print()
    print([x for x in p.iterdir() if x.is_dir()])
    print()

    PySources = list(p.glob("**/*.py"))
    for x in PySources:
        print(x)
    print()

    p.exists()
    p.is_dir()
    with p.open() as f: f.readline()

# import pdb
# import pickle
# import pickletools
# import pkgutil
# import platform
# import plistlib
# import poplib
from pprint import pprint
# import profile
# import pstats
# import py_compile
# import pyclbr
# import pydoc
# import queue
# import quopri
# import random
# import re
# import rlcompleter
# import runpy
# import sched
# import secrets
# import select
# import selectors
# import shelve
# import shlex
# import shutil
# import signal
# import site
# import sitecustomize
# import smtplib
# import socket
# import socketserver
# import sqlite3
# import ssl
# import stat
# import statistics
# import string
# import stringprep
# import struct
# import subprocess
# import symtable
import sys


# import sysconfig
# import syslog
# import tabnanny
# import tarfile
# import tempfile
# import test
# import textwrap
# import threading
# import time
# import timeit
# import tkinter
# import token
# import tokenize
# import tomllib
# import trace
# import traceback
# import tracemalloc
# import turtle
# import turtledemo
# import types
# import typing
# import unicodedata
# import unittest
# import urllib
# import usercustomize
# import uuid
# import venv
# import warnings
import wave
def test_wave():
    filename = "test.wav"

    with wave.open(filename, "wb") as wvw:
        wvw.setnchannels(1)

    with wave.open(filename, "rb") as wvr:
        wvr.getnchannels()


# import weakref
import webbrowser
def test_webbrowswer():
    url = "https://www.yolocounty.org/yolobuilds"
    webbrowser.open(url, new=2)


# import winreg
# import winsound
# import wsgiref
# import xdrlib
# import xml
# import xmlrpc
# import zipapp
import zipfile
def test_zipfile():
    data = b"""\
    Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
    nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
    sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
    pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
    Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
    felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
    dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""

    text = "test.txt"
    filename = "test.zip"
    with zipfile.ZipFile(filename, 'w') as f:
        f.write(text)

    with zipfile.ZipFile(filename, 'r') as f:
        with f.open(text) as myfile:
            print(myfile.read())


# import zipimport
# import zlib
# import zoneinfo

"""Third-Party Modules"""
# aiohttp             3.8.5
# aiosignal           1.3.1
# astroid             3.0.0
# async-timeout       4.0.3
# atomicwrites        1.4.1
# attrs               23.1.0
# Automat             22.10.0
# certifi             2023.7.22
# cffi                1.15.1
# charset-normalizer  3.2.0
# colorama            0.4.6
# constantly          15.1.0
# contourpy           1.1.1
# cryptography        41.0.4
# cssselect           1.2.0
# customtkinter       5.2.0
# cycler              0.11.0
# darkdetect          0.8.0
# dateutils           0.6.12
# docutils            0.20.1
# et-xmlfile          1.1.0
# ffmpeg              1.4
# filelock            3.12.4
# flake8              6.1.0
# fonttools           4.42.1
# frozenlist          1.4.0
# future              0.18.3
# hyperlink           21.0.0
# idna                3.4
# incremental         22.10.0
# iniconfig           2.0.0
# isort               5.12.0
# itemadapter         0.8.0
# itemloaders         1.1.0
# jmespath            1.0.1
# Kivy                2.2.1
# kivy-deps.angle     0.3.3
# kivy-deps.glew      0.3.1
# kivy-deps.sdl2      0.6.0
# Kivy-Garden         0.1.5
# kiwisolver          1.4.5
# lazy-object-proxy   1.9.0
# lxml                4.9.3
# matplotlib          3.8.0
# mccabe              0.7.0
# multidict           6.0.4
# numexpr             2.8.6
# numpy               1.26.0
# openpyxl            3.1.2
# packaging           23.1
# pandas              2.1.1
# pandastable         0.13.1
# parsel              1.8.1
# patsy               0.5.3
# Pillow              10.0.0
# pip                 23.2.1
# pluggy              1.3.0
# Protego             0.3.0
# py                  1.11.0
# pyarrow             13.0.0
# pyasn1              0.5.0
# pyasn1-modules      0.3.0
# pycodestyle         2.11.0
# pycparser           2.21
# PyDispatcher        2.0.7
# pyflakes            3.1.0
# pygame              2.5.2
# Pygments            2.16.1
# pyOpenSSL           23.2.0
# pyparsing           3.1.1
# pypiwin32           223
# PyQt6               6.5.2
# PyQt6-Qt6           6.5.2
# PyQt6-sip           13.5.2
# pytest              7.4.2
# python-dateutil     2.8.2
# python-tkdnd        0.2.1
# pytz                2023.3.post1
# pywin32             306
# queuelib            1.6.2
# requests            2.31.0
# requests-file       1.5.1
# scipy               1.11.2
# Scrapy              2.11.0
# screeninfo          0.8.1
# seaborn             0.12.2
# service-identity    23.1.0
# setuptools          65.5.0
# six                 1.16.0
# statsmodels         0.14.0
# tldextract          3.6.0
# ttkbootstrap        1.10.1
# ttkwidgets          0.13.0
# Twisted             22.10.0
# twisted-iocpsupport 1.0.4
# typing_extensions   4.7.1
# tzdata              2023.3
# urllib3             2.0.4
# w3lib               2.1.2
# watchdog            3.0.0
# wrapt               1.15.0
# xlrd                2.0.1
# yarl                1.9.2
# zope.interface      6.0

if __name__ == "__main__":
    main()