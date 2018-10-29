#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


fileList = []
matchList = []
dirPath = "./"
counts=0

def getsys():
    if os.name == "nt":
        #print("system is windows !" )
        cmd="move"
        return cmd
    else:
        #print("system is not windows !")
        cmd="mv"
        return cmd


def getListFiles(path):
     
    for root, dirs, files in os.walk(path):  
        for filespath in files:
            if ".txt" in filespath:
                fileList.append(os.path.join(root,filespath).replace("\n",""))
                #print (fileList[len(fileList)-1])
                
           
def getMatchTarget():
    #print "in getMatchTarget"
    global counts
    for each in range(0,len(fileList)):
        #print "in for"
            
        if fileList[each] != "":
            file=fileList[each]
            print("reading file: "+file)
            fl=open(file,"r")
            print("open file suscess....")
            #count=len(fl.readlines())
            #fl.seek(0,0)
            for line in fl.readlines():
                if 'StackTrace=' in line:
                    matchList.append(line.replace("\n",""))
                    print(line)
                    
            fl.close()
    counts=len(matchList)
    #print "out getMatchTarget"
                        
'''
                while fl.readline() != "":
                print(fl.readline())
                    
'''                    
def cmpLogCore(count,path):
    global matchList
    global fileList
    matchListTmp=[]
    fileListTmp=[]
    for each in range(1,len(matchList)):
        if (matchList[0] == matchList[each]):
            print(fileList[0]+" same with "+fileList[each]+"，move to type_"+str(count))
            cmd_tmp=getsys()+" "+path+fileList[each]+" "+path+"type_"+str(count)
            os.popen(cmd_tmp)
            
        else:
            #print(fileList[0]+" different with "+fileList[each])
            matchListTmp.append(matchList[each])
            fileListTmp.append(fileList[each])
    cmd_tmp=getsys()+" "+path+fileList[0]+" "+path+"type_"+str(count)
    os.popen(cmd_tmp)
    

    del matchList[:]    #0:len(matchList)
    del fileList[:]     #0:len(fileList)
    matchList=matchListTmp[:]
    fileList=fileListTmp[:]
    del matchListTmp[:]
    del fileListTmp[:]
    



def cmpLog(path):
    count=0
    while True:
        if (len(matchList)<2 and len(fileList)>0):
            os.mkdir(path+"type_"+str(count))
            cmd_tmp=getsys()+" "+path+fileList[0]+" "+path+"type_"+str(count)
            os.popen(cmd_tmp)
            break
        if len(fileList)>0:
            os.mkdir(path+"type_"+str(count))
            cmpLogCore(count,path)
            count=count+1
        else:
            break
    print("Move %s files in total !" %counts)

    
                
                
if __name__=="__main__":
    getListFiles(dirPath)
    #print (fileList)
    getMatchTarget()
    cmpLog(dirPath)
    

