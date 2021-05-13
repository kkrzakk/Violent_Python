import optparse
import socket

def connection_Scan(target_host, target_port):
	try:
		connection = socket.socket(AF_INET, SOCK_STREAM)
		connection.connect((target_host,target_port))
		connection.send('Testing Connction')
		results = connection.recv(100)
		print('[+] %d - tcp open [+]'% target_port)
		connection.close()
	except:
		print('[+] %d - tcp closed [+]'% target_port)

def port_scan(target_host, target_ports):
	try:
		target_IP = socket.gethostbyname(target_host)
	except:
		print('[-] Unknown Host [-]')
		return
	try:
		target_name=socket.gethostbyaddr(target_IP)
		print('[+] Scan Results for: %s [+]'% target_Name[0])
	except:
		print('[+] Scan Results for: %s [+]'% target_IP)
	setdefaulttimeout(1)
	for target_port in target_ports:
		print('Scanning port %d'% target_port)
		connection_Scan(target_host, int(target_port))

def main():
	usage = 'usage %prog –h <target host> -p <target port>'
	parser = optparse.OptionParser(usage=usage)
	parser.add_option('-h', dest='target_host', type='string',\
		help='specify target host')
	parser.add_option('-p', dest='target_port', type='int',\
		help='specify target port[s]')
	(options, args) = parser.parse_args()
	target_host = options.target_host
	target_port = options.target_port
	if (target_host == None) | (target_port == None):
		print(parser.usage)
		exit()


if __name__ ==' __main__':
	main()