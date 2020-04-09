
#/usr/bin/python3
import pefile
import hashlib
import colorama
import os
import sys
import platform
from os import execv


def checksum():
    #Ask for the file location, will be used to calculate md5 as well
    pathtoexe = input("Please provide location to exe or dll")


    if str(os.path.exists(pathtoexe)):
        with open(pathtoexe, 'rb') as filecalculate:
            print("Calculating\n")
            read = filecalculate.read()
            listhash = [hashlib.md5(read).hexdigest(), hashlib.sha1(read).hexdigest(), hashlib.sha256(read).hexdigest()]

            print("MD5:\n" + listhash[0] + "\n","SHA1:\n" + listhash[1] + "\n","SHA256:\n" + listhash[1] + "\n")
    elif not str(os.path.exists(pathtoexe)):
        #including restart
        print("File not found\n")

        print("Please provide a correct path")

        Operatingsystem = platform.system()

        if Operatingsystem == "Windows":

            os.execv(sys.executable, ['python'] + sys.argv)
            return checksum()
        elif Operatingsystem == "Linux":
            return checksum()
            os.execv(__file__, sys.argv)

checksum()
