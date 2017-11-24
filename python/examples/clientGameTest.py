#!/usr/bin/env python
# coding: utf-8

import socket
import time
import sys
import random

hote = "localhost"
port = 10000

server_address = (hote, port)
def sendCommand(cmd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "Connection on {}".format(port)
    sent = sock.sendto(cmd, server_address)
    print("Command ", cmd, " sent")
    sock.close()
    time.sleep(0.5)

if __name__ == '__main__':
    sendCommand("(0)")
    for x in range(40):
        sendCommand("("+str(random.randint(1,2))+")")

