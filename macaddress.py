import time
import sys
import subprocess
import os
import base64
import uuid
import datetime
import traceback
import base64
import json
from time import gmtime, strftime
import math
import random, string
import time
import psutil
import uuid 
from getmac import get_mac_address

# Importing socket library 
import socket 

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
  
# Function to display hostname and 
# IP address 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  
# Driver code 
get_Host_name_IP() #Function call 
  
eth_mac = get_mac_address(interface="eth0")
host_mac = get_mac_address(hostname="princeton0")

print('eth mac {0}'.format(str(eth_mac)))

print('host mac {0}'.format(str(host_mac)))

print (hex(uuid.getnode())) 


print ("The MAC address in formatted way is : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 

print("PSUTIL")
print(psutil_iface('eth0'))

start = time.time()
uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
end = time.time()
row = { }
row['host'] = os.uname()[1]
row['end'] = '{0}'.format( str(end ))
row['te'] = '{0}'.format(str(end-start))
row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
row['cpu'] = psutil.cpu_percent(interval=1)
usage = psutil.disk_usage("/")
row['diskusage'] = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
row['memory'] = psutil.virtual_memory().percent
row['id'] = str(uuid2)
json_string = json.dumps(row)
print(json_string)
