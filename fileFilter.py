#!/usr/bin/python
import sys
import subprocess
outputFile="C:/Yingming Fang/project/outPut.txt"
prefix="sub"
hdfs_dir="/user/yingming.fang2/dirFilter"

hdfs_com =['hadoop','fs','-ls',hdfs_dir]

outfile = open(outputFile,'w+')
subprocess.call(hdfs_com,stdout=outfile)

part = sys.argv[1]
totalcontend=outfile.readlines()

for file in totalcontend:
	if file.endswith('.json') == False:
		totalcontend.remove(file)
		
print totalcontend