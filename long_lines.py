#!/usr/bin/python
from sys import argv
import os
import sys
 
scriptName, firstArg, secondArg = argv
  
#print ("script name: ", script)
#print ("file: ", first)
#print ("line_len: ", second)

inFileName = str(firstArg)
maxLineLen = int(secondArg)# 110

def exists(path):
    try:
        f = open(path)
        f.close()
        #print path + " exist"
        return True
    except IOError:
        #print path + " missing"
        return False

if False==exists(inFileName):
    print inFileName + " absents"
    sys.exit()


my_file = open(str(inFileName),'r')
line = my_file.readline()
lineCnt = 1;
while line:
    curLenOfLine = len(line)
    #print inFileName +" "+ str( lineCnt) + ' '+ str(len(line))
    if maxLineLen < curLenOfLine: 
        print inFileName +" "+ str( lineCnt) + ' '+ str(len(line)) +' '+line[:-1]
        #print len(line)
        #print line
    
    line = my_file.readline()
    lineCnt = lineCnt+1

my_file.close()

if __name__ == "__main__":
    print ("Start")
