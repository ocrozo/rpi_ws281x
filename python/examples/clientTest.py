#!/usr/bin/env python
# coding: utf-8

import socket

hote = "localhost"
port = 10000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(u"(0)")

print "Close"
socket.close()
