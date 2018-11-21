import os
import sys
import subprocess
#dir = 'C:/Yingming Fang/verify'
#fi = open(dir+os.sep+'adminB.txt','Ur+')
#fo = open(dir+os.sep+'adminTest.txt','Ur+')
def fileComp(input, output,log):
	log.write('----------------------beg-----------------------'+'\n')
	start = input.rfind('/')
	filename = input[start+1:len(input)]
	log.write('benchmark file is :'+input+'\n')
	log.write('cmp file is '+output+'\n')
	fi = open(input,'Ur+')
	fo = open(output,'Ur+')
	benchmark = fi.readlines()
	out = fo.readlines()
	print "items in bechmark: %s are %s" % (input,str(len(benchmark)))
	log.write('items in bechmark:'+str(input)+' is :'+str(len(benchmark))+'\n')
	print "item in outfile: %s are %s " % (output,str(len(out)))
	
	log.write('items in outfile:'+str(output)+' is :'+str(len(out))+'\n')
	count =0
	for each in benchmark:
		flag=0
		for single in out:
			if each.strip()==single.strip():
				flag=1
				count=count+1
		if flag==0:
                	print "file:%s is existed in benchmark, which is not contained in the outfile" %each
			log.write('file:'+str(each).strip()+' is existed in benchmark, which is not contained in outputfile'+'\n')
	print 'there are %d items contained in output file ' %count
	log.write('there are:'+str(count)+' items contained in output file'+'\n')
	fi.close()
	fo.close()
	log.write('delete file:'+input+'\n')
	subprocess.call(['rm',input])
	log.write('delete file:'+output+'\n')
	subprocess.call(['rm',output])
	log.write('--------------------end-------------------------'+'\n'+'\n')

par1 = sys.argv[1]
par2 = sys.argv[2]
filelist = os.listdir(par1)
logfile ='log.txt'
log =open(logfile,'w+')
log.write('---------log is start----------'+'\n')
for file in filelist:
	start = file.rfind('/');
	filename = file[start+1:len(file)]
	print filename
	inputfile=filename+'B.txt'
	cmpfile=filename+'Test.txt'
	input = open(inputfile,'w+')
	output = open(cmpfile,'w+')
	subprocess.call(['ls',par1+os.sep+filename],stdout=input)
	subprocess.call(['ls',par2+os.sep+filename],stdout=output)
	fileComp(inputfile,cmpfile,log)
	input.close()
	output.close()
log.write('---------log is ended----------'+'\n')
log.close()
#	fileComp(input+os.sep+filename,output+os.sep+filename,log)

