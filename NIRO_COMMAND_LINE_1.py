import socket
import whois
import time, sys

print(r''' 
NNNNNNNN        NNNNNNNNIIIIIIIIIIRRRRRRRRRRRRRRRRR        OOOOOOOOO     
N:::::::N       N::::::NI::::::::IR::::::::::::::::R     OO:::::::::OO   
N::::::::N      N::::::NI::::::::IR::::::RRRRRR:::::R  OO:::::::::::::OO 
N:::::::::N     N::::::NII::::::IIRR:::::R     R:::::RO:::::::OOO:::::::O
N::::::::::N    N::::::N  I::::I    R::::R     R:::::RO::::::O   O::::::O
N:::::::::::N   N::::::N  I::::I    R::::R     R:::::RO:::::O     O:::::O
N:::::::N::::N  N::::::N  I::::I    R::::RRRRRR:::::R O:::::O     O:::::O
N::::::N N::::N N::::::N  I::::I    R:::::::::::::RR  O:::::O     O:::::O
N::::::N  N::::N:::::::N  I::::I    R::::RRRRRR:::::R O:::::O     O:::::O
N::::::N   N:::::::::::N  I::::I    R::::R     R:::::RO:::::O     O:::::O
N::::::N    N::::::::::N  I::::I    R::::R     R:::::RO:::::O     O:::::O
N::::::N     N:::::::::N  I::::I    R::::R     R:::::RO::::::O   O::::::O
N::::::N      N::::::::NII::::::IIRR:::::R     R:::::RO:::::::OOO:::::::O
N::::::N       N:::::::NI::::::::IR::::::R     R:::::R OO:::::::::::::OO 
N::::::N        N::::::NI::::::::IR::::::R     R:::::R   OO:::::::::OO   
NNNNNNNN         NNNNNNNIIIIIIIIIIRRRRRRRR     RRRRRRR     OOOOOOOOO     
                                                                       
 ''')	



urlIn = input("Put URL here. FOR EXAMPLE www.google.com:")
ip = str(socket.gethostbyname(urlIn))

	

#Give the IP addr of url/domain
# THIS CODE NEEDS WORK
def getIP(url):
	try:
		sockw= socket.gethostbyname(url)
		print("IP ADDRESS IS:",sockw)
	except:
		print("Unable to find IP Address for your URL")
	

#give a lists of ip addr the url uses, and url for ip addr
def getMoIP(url):
	try:
		sockl = socket.gethostbyname_ex(url)
		print(sockl)
	except:
		print("Unable to find any information")
		
# print url or ip whois/LOOKUP info		
def getWhois(url):
	try:
		domain = whois.whois(url)
		print(domain)
	except:
		print("Domain does not exist")

#SOCKET PORT SCANNER
def portScanner():
		#some commun tcp/udp ports
		hosts = [ip]
		ports = [7, 20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 143, 443, 3389, 8008]

		for host in hosts:
			for port in ports:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(5)
			
					result = s.connect_ex((host, port))
					if result == 0:
						print("PORT:", port,"OPEN", "-->","SERVICE:", str(socket.getservbyport(port,'tcp')), "\n")
					else:
						print("PORT:", port,"CLOSE\n")
					s.close()
				except:
					pass
					
def animation():
	animation = "*#$%^&*\n" 

	for i in range(25):
		time.sleep(0.1)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()
	print("\nSTART\n")

#the functions	
animation()	
getIP(urlIn)
animation()
getMoIP(urlIn)
animation()
getWhois(urlIn)
animation()
portScanner()


