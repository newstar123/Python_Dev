#!/usr/bin/python
import sys
import subprocess
import os
import threading
import time
class JsonBsonConvert (threading.Thread):
    def __init__(self, threadID, name, filename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.file = filename
    def run(self):
        print "Starting " + self.name
        json2bson(self.threadID,self.name, self.file)
        print "Exiting " + self.name

def json2bson(threadId,threadName, filename):
    print "[thread name:%s thread id:%s start: %s" % (threadName, threadId,time.ctime(time.time()))
    input = open(filename,'r+')
    contends = input.readlines()
    for i in range(len(contends)):
                    start = contends[i].rfind('/')+1
                    end = contends[i].rfind('.')
                    fileName = contends[i][start:end]
                    print fileName
                    subprocess.call(['sh','convertBson.sh',fileName])
    input.close()
    print "[thread name:%s thread id:%s start: %s" % (threadName, threadId,time.ctime(time.time()))


print 'python executes start time:%s',time.ctime(time.time())
pythonlog = open ('python_json_bson_log.txt','a')
pythonlog.write('python executes start time: '+ str(time.ctime(time.time()))+'\n')
outputFile="outPut.txt"
prefix="sub"
hdfs_dir="/projects/assetcommander/lhp_product/output/frontend_product_2_outputs"
hdfs_com =['hadoop','fs','-ls',hdfs_dir]

outfile = open(outputFile,'w+')
subprocess.call(hdfs_com,stdout=outfile)
outfile.close()

inputfile = open(outputFile,'r+')
part = int(sys.argv[1])
totalcontend=inputfile.readlines()
for file  in totalcontend:
	if file.endswith('.json') == False:
		totalcontend.remove(file)

		
section = len(totalcontend)/int(part)
start = 0
allFiles=[]


for i in range(part):
    inputFile = prefix+str(i)
    input = open(inputFile,'w+')
    pythonlog.write(str(time.ctime(time.time()))+'add sub file: '+inputFile+'\n')
    allFiles.append(inputFile)
    if i<part-1:
        input.writelines(totalcontend[i*section:i*section+section])
    else:
        input.writelines(totalcontend[i*section:len(totalcontend)])
    input.close()

inputfile.close()
threads = []
for i in range(len(allFiles)):
    threadname = "Thread-"+str(i)
    threads.append(JsonBsonConvert(i, threadname, allFiles[i]))
print 'start to execut sub thread'
pythonlog.write(str(time.ctime(time.time()))+'start to execut sub thread' +'\n')
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
print 'python executes end time:%s',time.ctime(time.time())
pythonlog.write('python executes end time:'+str(time.ctime(time.time()))+'\n')

print 'start to delete temporary files'
for i in range(len(allFiles)):
    subprocess.call(['rm',allFiles[i]])
    print 'delete file %s' %(allFiles[i])
    pythonlog.write(str(time.ctime(time.time()))+'delete file: ' +allFiles[i]+'\n')

subprocess.call(['rm',outputFile])
print 'delete file %s' %(outputFile)
pythonlog.write(str(time.ctime(time.time()))+'delete file: ' +outputFile+'\n')
print "Exiting Main Thread"
pythonlog.write(str(time.ctime(time.time()))+'Exiting Main Thread'+'\n')
pythonlog.close()
