import os
import time 

print ("open compsec ubuntu 19.10 edition")
time wait(3)
print ("welcome to compsec 1.0 made by n7co")
print ("1.run compsec")
print ("2.quit")
ch = raw_input("please select a option")
if ch == '1'
	os.system("sudo apt-get update")
	os.system("sudo apt-get upgrade")
	os.system("sudo apt-get install rkhunter")
	os.system("sudo rkhunter --update")
	os.system("sudo rkhunter --check")
	print("installed and ran rkhunter")
	os.system("sudo apt-get install aptitiude")
	os.system("sudo apt-get install ufw")
	os.system("sudo ufw enable")
