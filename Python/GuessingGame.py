import random
import json

fileName = 'config.js'
print 'Helo World'
file = open(fileName, 'rw')

#Parse jsonObject 
jsonObject = json.load(file)
print jsonObject
print jsonObject["hello"]

#Read in a file line by line
for line in file.readlines():
	print line