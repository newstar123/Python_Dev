#!/usr/bin/python
'''
this script is used to convert specified  files to particular suffix files
'''
import os

dir='/home/yingming.fang/project/json2bson/positionsUi.json'
#dir='C:/Yingming Fang/project/Python/gitPython'
def filterFile(s,*endstring):
        array = map(s.find,endstring)
        if -1 in array:
                return False
        else:
                return True


s = os.listdir(dir)
f_file = []
for i in s:
	if filterFile(i,'part-r-'):
#		print i
		os.rename(dir+os.sep+i,dir+os.sep+i+'.json')


