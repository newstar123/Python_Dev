import os
from io import open
'''
convert \r to \n in order to be used in the unix environment
'''
dir ='C:\\Yingming Fang\\project\\Python\\gitPython\\'
collections = os.listdir(dir)

for ins in collections:
	if ins.endswith('.txt')==True:
		print dir+ins
		f = open(dir+ins,'rb+')#can't be replaced as "wb+"
		str = f.read()
		str=str.replace('\r','\n')
		f.seek(0,0)# it is used to move the cursor to the begining of the file
		f.truncate()# clear all the contends from the cursor
		f.write(str)
		f.close()

