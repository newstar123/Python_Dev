import os
'''
	find specified files in a document
'''
dir='C:\Dell'
suffix='mst'
result=os.walk(dir)
fileList=[]
for single in result:
	for p in single[2]:
		if p.endswith(suffix):
			fileName=os.path.join(single[0],p)
			fileList.append(fileName)
			print fileName

			
