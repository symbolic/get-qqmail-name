import urllib
base = 'https://ssl.zc.qq.com/cgi-bin/chs/qqmailreg/check_mail?email='
end = '@qq.com'

def main():
	#fp1 = open('result.log', 'a')
	fp2 = open('password.txt', 'r')
	
	param = fp2.readline()[:-1]
	while len(param) > 1:
		domain_name = base + param + end
		tempStr = urllib.urlopen(domain_name).read()
		
		if 'exist' not in tempStr:
			fp1 = open('result.log', 'a')
			print '>'*10 + param
			fp1.write(param + '\t')
			#print len(urllib.urlopen(domain_name).read())
			fp1.write('' + str(len(tempStr)) + '\t')
			
			#print urllib.urlopen(domain_name).read()
			fp1.write(tempStr + '\n')
			fp1.close()
		
		param = fp2.readline()[:-1]
		
	fp2.close()
	
	print 'finished'
if __name__ == '__main__':
	main()