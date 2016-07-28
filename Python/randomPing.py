import os
from GenRandNums import GenerateIp

def PingIp(hostname):
  response = os.system("ping -c 1 " + hostname + "> ~/Desktop/PingOutput.txt")

  #and then check the response...
  if response == 0:
    print hostname, 'is up!'
  else:
    print hostname, 'is down!'


hostname = GenerateIp()#"216.58.218.110" #example
print "Generated IP: "+ hostname
PingIp(hostname)