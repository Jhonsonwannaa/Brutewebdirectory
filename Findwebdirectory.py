

import requests
import sys
import pyfiglet as pyg  

res= pyg.figlet_format("Ys jhonson le wana !!!!!" , font="banner3")
print(res)


sos = sys.argv[1]
sy = sys.argv[2]
	
dab = open(sy, 'r')

print 

try :
	for line in dab.readlines():
		
		da = line.strip()
		req = requests.Session()
		bad = req.get('http://'+sos+'/'+da)
		result =bad.url+' '+str(bad.status_code)
		
		if '200' in result:
			man = bad.status_code
			class couleur:
			 OK = '\033[92m' #GREEN
			 WARNING = '\033[93m' #YELLOW
			 FAIL = '\033[91m' #RED
			 RESET = '\033[0m' #RESET COLOR
			print(couleur.OK+result)
			
		if '404' in result :
			class couleur:
			 OK = '\033[92m' #GREEN
			 WARNING = '\033[93m' #YELLOW
			 FAIL = '\033[91m' #RED
			print(couleur.FAIL+result)
			
			
			
except :
	print('python dirsearch.py target wordlist.txt')

