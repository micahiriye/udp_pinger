#-----------------------------------------------
# Title: UDPClient.py
# Author: Kenny Keating
# Abstract: *NOTE* this was written in python2.7 
#	    This will simulate a client pinging a server 10 times
#	    and will display the RTT of each packet. If the packet
#	    is lost then a time out message will display.The min,
#	    max, and average RTT's will be displayed along with 
#	    the percent of packet loss   
# Date:11/12/14 
#
#------------------------------------------------

#used for showing percentage 
from __future__ import division
from socket import *
from time import *

#Creates a socket for UDP packets
clientSocket = socket(AF_INET,SOCK_DGRAM)
#This will be on a local machine
host = 'localhost' 
#Set port to 9001, same as the server and it's over 9000!
port = 9001
#message for server code to upper case 
message = ("the port is over 9000!")
#create a list to store each successful RTT 
results = []
#Timeout is set to 1 second
clientSocket.settimeout(1)
#Counter to count pings
counter=1

#Sends only 10 pings
while counter<11:
	
	#Assigns the current time in seconds and is returned as a floating point num
	startTime = time()

	#Send packet with message to server
	clientSocket.sendto(message, (host,port))
	try:
		#Receive the packet from the server
		message, address = clientSocket.recvfrom(1024)
		#Calculates difference from start time giving RTT
		RTT = (time()-startTime)
		print "Ping", counter
		print "RTT: " , RTT , "seconds\n"
		counter+=1
		#add successful RTT's to list
		results.append(RTT)
	#If RTT is greater than 1 second, do the following
	except timeout:
		print "Ping ", counter
		print  "Request timed out\n"
		counter+=1
	if counter >10:
		clientSocket.close()
		#sort list of times in ascending order
		results.sort()
		print "Min RTT: ", results[0],"seconds"
		#Get list size to print max RTT
		length = len(results)
		print "Max RTT: ", results[length-1], "seconds"
		sum = 0
		for i in results:
			sum = sum +i
		avg = sum/length
		print "Average RTT: ", avg,"seconds"
		percentLoss =100- (length/(counter -1))*100
		#Format the percent to precision 2 e.g. 79
		print "Packet loss rate = ", '{0:.2g}'.format(percentLoss) , "%"
		print "\nClient socket closed."
