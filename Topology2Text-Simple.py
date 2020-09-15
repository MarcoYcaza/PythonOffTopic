import pandas as pd
import os

mList=os.listdir("CAJAMARCA_ICA")

#There is a function f = open("myfile","read").read()

#mReadedFiles = [open(f,encoding="utf8",errors='ignore').read() for f in mList]


mReadedFiles = [open('CAJAMARCA_ICA/'+f,'r').read() for f in mList]

mExtractedMaps = [e[e.find("+---"):e.find("q!!")] for e in mReadedFiles]

mExtractedNames =  [k[k.find("\n\n")+2:len(k)-2] for k in mExtractedMaps]

newList = list(zip(mExtractedMaps,mExtractedNames))

allFiles = open("myFile.txt","w+")

for i in newList:
    
    allFiles.write("\n######################################################################\n")
    allFiles.write(i[1])
    allFiles.write("\n")
    allFiles.write(i[0])
    allFiles.write("\n")
    allFiles.write("\n######################################################################\n")
allFiles.close()


