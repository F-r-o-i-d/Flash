import socket, argparse, sys, threading
parser = argparse.parser(sys.argv)
port_to_scan = []
print("\033c")
print("""

\t    ________           __  
\t   / ____/ /___ ______/ /_ 
\t  / /_  / / __ `/ ___/ __ \\
\t / __/ / / /_/ (__  ) / / /
\t/_/   /_/\\__,_/____/_/ /_/ 
\t                       a new modern port scanner

""")
if not parser.IfExist("-a"):
	print("usage fash [option]")
	print("\t-a : ip       (required)")
	print("\t-t : thread   (optional)")
	print("\t-p : max-port (optional)")
	exit()
threadNumber = parser.GetValueOf("-t")
maxport = parser.GetValueOf("-p")
if maxport == None:
    maxport = 10000
maxport = int(maxport)
if threadNumber == None:
	threadNumber = int(0.4 * maxport)
else:
	threadNumber = int(threadNumber)
ip = str(parser.GetValueOf("-a"))
for x in range(int(maxport)):
	port_to_scan.append(x)
split_indice = int(len(port_to_scan) / threadNumber)
i = 1
index = 0
port = []
for x in range(threadNumber):
	port.append(list())
for x in range(len(port_to_scan)):
	i += 1
	try:
		port[index].append(x)
		if i >= split_indice:
			index += 1
			i = 1
	except IndexError:
		pass
open_port = []
def scan(*args):
	list_port = args[0]
	for port in list_port:
		try:
			s = socket.socket()
			s.settimeout(1)
			s.connect((ip,port))
			s.close()
			open_port.append(port)
		except ConnectionRefusedError:
			pass
		except socket.timeout:
			pass
		except socket.gaierror:
			break
		
for x in range(threadNumber-2):
	processThread = threading.Thread(target=scan, args=[port[x]]) 
	processThread.start()
scan((port[threadNumber-1]))
open_port.sort()
print("\topen port :")
for port in open_port:
	print("\t\t" + str(port))
