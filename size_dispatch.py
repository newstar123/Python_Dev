import os
import sys
import subprocess
import threading
import time
# the main function of multithread
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
		print contends[i]
		subprocess.call(['sh','convertBson.sh',contends[i].strip()])
    input.close()
    print "[thread name:%s thread id:%s start: %s" % (threadName, threadId,time.ctime(time.time()))
# thread used to extract  the name of each table
def getFile(item):
	line = item[1]
	m = line.rfind('/')+1
	n = line.rfind('.')
	return line[m:n]+'\n'

print 'python executes start time:%s',time.ctime(time.time())
pythonlog.write('python executes start time: '+ str(time.ctime(time.time()))+'\n')
pythonlog = open ('python_json_bson_log.txt','a')	
hadoop_trace="/projects/assetcommander/lhp_product/output/frontend_product_2_outputs"
# file used to store each table and the the total size of each table.
tempfile ="out"
temp = open(tempfile,'w+')
fileList=['hadoop','fs','-du',hadoop_trace]
# get each table
pythonlog.write(str(time.ctime(time.time()))+'start to retrive the files'+'\n')
subprocess.call(fileList,stdout = temp)
fileSize=['hadoop','fs','-dus',hadoop_trace]
# get total size of all the tables
pythonlog.write(str(time.ctime(time.time()))+'start to get the total sizes of the files'+'\n')
subprocess.call(fileSize,stdout = temp)
temp.close()
# the prefix of each table block
prefix="sub"
file = open(tempfile,'Ur+')
items = file.readlines()
# get total size
totalSize=long(items[len(items)-1].split()[1])
# get the size of each block
threadcount = int(sys.argv[1])
pythonlog.write( str(time.ctime(time.time()))+'python thread count:'+ str(threadcount)+'\n')
single = totalSize/threadcount
print single
print totalSize
items = items[1:len(items)-1]
for i in range(len(items)):
	items[i]= tuple(items[i].split())
print items[0]
pythonlog.write(str(time.ctime(time.time()))+'start to sort the files by sizes'+'\n')
items.sort(key=lambda item:long(item[0])) 
k=0
allFiles=[]
# start to divide the total tables into some blocks
for i in range(threadcount):
	fileName=prefix+str(i)
	fileOpen=open(fileName,'w+')
	j=k
	singleSize=0
	pythonlog.write(str(time.ctime(time.time()))+'add sub file: '+fileName+'\n')
	allFiles.append(fileName)
	while j< len(items):
		print j
		singleSize = singleSize+long(items[j][0])
		fileOpen.write(getFile(items[j]))
		j = j+1
		if singleSize>single:
			pythonlog.write(str(time.ctime(time.time()))+'sub file: '+fileName+':total file count: '+str(j-k)+'\n')
			k = j
			fileOpen.close()
			break
 
# start	 to create new threads
threads=[]
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
pythonlog.write('start to delete temporary files'+'\n')
for i in range(len(allFiles)):
    subprocess.call(['rm',allFiles[i]])
    print 'delete file %s' %(allFiles[i])
    pythonlog.write(str(time.ctime(time.time()))+'delete file: ' +allFiles[i]+'\n')

subprocess.call(['rm',tempfile])
print 'delete file %s' %(tempfile)
pythonlog.write(str(time.ctime(time.time()))+'delete file: ' +tempfile+'\n')
print "Exiting Main Thread"
pythonlog.write(str(time.ctime(time.time()))+'Exiting Main Thread'+'\n')

'''			
j=0
while j< len(items):
	items[j]= (' ').join(list(items[j]))+'\n'
	j=j+1
'''
file.close()
print "Exiting Main Thread"
pythonlog.write(str(time.ctime(time.time()))+'Exiting Main Thread'+'\n')
pythonlog.close()