import requests
import os
import os,sys
import multiprocessing
import threading

url_array= ["https://api.github.com","http://bilgisayar.mu.edu.tr/",
            "https://www.python.org/","http://akrepnalan.com/ceng2034",
            "https://github.com/caesarsalad/wow"]

#check the url 
print("200 = Successful, 404 and 505 = Failed\n")	
def requester(url):
	response = requests.get(url)
	print(url,response.status_code)
	
thread1 = threading.Thread(target = requester,args=("https://api.github.com",))
thread2 = threading.Thread(target = requester,args=("http://bilgisayar.mu.edu.tr/",))
thread3 = threading.Thread(target = requester,args=("https://www.python.org/",))
thread4 = threading.Thread(target = requester,args=("http://akrepnalan.com/ceng2034",))
thread5 = threading.Thread(target = requester,args=("https://github.com/caesarsalad/wow",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

while(True):
	if(thread5.is_alive()):
		continue
	#printing PID
	pıd = os.getpid()
	print("\nPID value:",pıd)		

	#printing loadavg 5 minutes
	load1,load5,load15 = os.getloadavg()
	print("\nLoadavg 5 minutes:",load5)

	#printing nproc
	nproc=multiprocessing.cpu_count()
	print("\nNproc value:",nproc)			

	#printing loadavg:
	loadavg=os.getloadavg()
	print("\nLoadavg value",loadavg)

	print("\nProgram will end itself if (nproch-loadavg<5)")
	while(True):					
		load1,load5,load15 = os.getloadavg()	
		if((nproc-load5)<1):			
			break				
				
		
		














