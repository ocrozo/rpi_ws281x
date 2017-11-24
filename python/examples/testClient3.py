import socket
import sys
import time
# Create a UDP socket

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'
i=0
while (True):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send data
        print >>sys.stderr, 'sending "%s"' % message+str(i)
        sent = sock.sendto(message+str(i), server_address)
	i=i+1
	time.sleep(1)
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
