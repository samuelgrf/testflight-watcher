#!/usr/bin/python
import sys
from subprocess import Popen
from time import sleep

COMMAND = ['python'] + sys.argv[1:]

while True:
    print('\nRestarting:', COMMAND)
    p = Popen(COMMAND) # shell=True
    p.wait()
    sleep(10)
