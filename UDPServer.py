#-----------------------------------------------
#
# Title: UDPServer.py
# Author: Kenny Keating
# Abstract: This will act as a server to receive pings from a client
#	    and simulate packet loss.  
# Date: 11/12/13
#
#-----------------------------------------------

# We will need the following module to generate randomized lost packets

import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('localhost', 9001))
print "Server socket initialized\nAwaiting connection..."
while True:
	# Generate random number in the range of 0 to 10
	rand = random.randint(0, 10)
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	# Capitalize the message from the client
	message = message.upper()
	# If rand is less is than 4, we consider the packet lost and do not respond
	#prints message sent from client in all uppercase
	print message
	if rand < 4:
		continue
		# Otherwise, the server responds
	serverSocket.sendto(message, address)


