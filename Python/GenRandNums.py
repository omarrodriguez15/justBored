import random
from datetime import datetime

craziness = 100

def GetSetOfNumbers(min, max, postFix):
    num = ""
    numOfDigits = (random.randint(0, craziness) % max) + 1
    while numOfDigits < min:
        numOfDigits += 1
    for x in range(0, numOfDigits):
        num += str(random.randint(0, 9))
    if postFix:
        num += "."
    return num

def GenerateIp():
    random.seed(datetime.now())
    ip = GetSetOfNumbers(2, 3, True) + GetSetOfNumbers(2, 3, True) + GetSetOfNumbers(2, 3, True) + GetSetOfNumbers(2, 3, False)
    return ip
