#!/usr/bin/env python
# coding: utf-8

import socket
import time
import sys
import random

hote = "localhost"
port = 10000

def sendCommand(cmd):
    scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scket.connect((hote, port))
    print "Connection on {}".format(port)

    scket.send(u"(0)")
    print("Command ", cmd, " sent")
    #print "Close"
    scket.close()
    time.sleep(0.5)

if __name__ == '__main__':
    sendCommand("(0)")
    for x in range(40):
        sendCommand("("+str(random.randint(1,2))+")")

