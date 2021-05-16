import optparse
from socket import *

def connection_Scan(target_host, target_port):
	try:
		connection = socket(AF_INET, SOCK_STREAM)
		connection.connect((target_host,target_port))
		connection.send('Testing Connection')
		results = connection.recv(100)
		print('[+] %d - tcp open [+]'% target_port)
		print('[+] %s'% str(results))
		connection.close()
	except Exception as e:
		print(e)
		print('[+] %d - tcp closed [+]'% target_port)

def port_scan(target_host, target_ports):
	try:
		target_IP = gethostbyname(target_host)
	except:
		print('[-] Unknown Host [-]')
		return
	try:
		target_name=gethostbyaddr(target_IP)
		print('[+] Scan Results for: %s [+]'% target_Name[0])
	except:
		print('[+] Scan Results for: %s [+]'% target_IP)
	setdefaulttimeout(1)
	for target_port in target_ports:
		print('Scanning port %s'% target_port)
		connection_Scan(target_host, int(target_port))

def main():
	usage = '%prog –H <target host> -p <target port>'
	parser = optparse.OptionParser(usage=usage)
	parser.add_option('-H', dest='target_host', type='string',\
		help='specify target host')
	parser.add_option('-p', dest='target_port', type='string',\
		help='specify target port[s]')
	(options, args) = parser.parse_args()
	target_host = options.target_host
	target_port = str(options.target_port).split(',')
	if (target_host == None) | (target_port == None):
		print(parser.usage)
		exit()
	port_scan(target_host,target_port)


if __name__ =='__main__':
	main()