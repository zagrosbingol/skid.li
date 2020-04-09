#add an option where the user can specify where to save output
#/usr/bin/python3
import pefile
import re
import os
import random
from datetime import date
import time


#test conctatenation
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)


def portable():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
        #Ask for the file location, will be used to calculate md5 as well
    pathtoexe = input("Please provide location to exe or dll")
    currentdirectory = os.getcwd()
    filename = pathtoexe
    for i in range(2):
        numbers = random.randint(1, 200)
    output = os.path.join(currentdirectory, "pedump"+str(date.today())+"-"+str(numbers)+".txt")
    #output = os.path.join(currentdirectory, "pedump"+".txt")

    f = open(output, "w")
    #handle and Parse the pefile
    exefile = pefile.PE(pathtoexe, fast_load=True)
    print("Dumping!")

    fulldump = exefile.dump_info()
    f.write(fulldump)
    f.close()
    

portable()
    
