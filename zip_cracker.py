import zipfile
import optparse
from threading import Thread

def extract_zip(zip_file, password):
	try:
		zip_file.extractall(pwd=password.encode())
		print('[+] PASSWORD: ' + password + ' [+]')
	except:
		pass 

def main():
	usage='usage%prog ' +\
		'-f <zip_file> -d <dictionary>'
	parser= optparse.OptionParser(usage=usage)
	parser.add_option('-f', dest='zfile', type='string',\
		help='Add Zip File')
	parser.add_option('-d', dest='dictionary', type='string',\
		help='Add Dictionary')
	(options, args) = parser.parse_args()
	if (options.zfile == None) | (options.dictionary == None):
		print(parser.usage)
		exit()
	else:
		zfile=options.zfile
		dictionary=options.dictionary
	zip_file = zipfile.ZipFile(zfile)
	passwords_file = open(dictionary)
	for row in passwords_file.readlines():
		password=row.strip('\n')
		attempt=Thread(target=extract_zip, args=(zip_file, password))
		attempt.start()
		

if __name__=='__main__':
	main()