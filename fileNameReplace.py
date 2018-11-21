#!/usr/bin/python
'''
this script is used to convert specified suffix files to no suffix files
'''
import os

dir='C:\\Python\\'
def filterFile(s,*endstring):
        array = map(s.endswith,endstring)
        if True in array:
                return True
        else:
                return False


s = os.listdir(dir)
f_file = []
for i in s:
	if filterFile(i,'.txt','t'):
		print i
		index  = i.index('.')
		print i[:index]
		os.rename(dir+os.sep+i,dir+os.sep+i[:index])


