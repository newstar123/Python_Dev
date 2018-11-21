#!/usr/bin/python
import json
import sys
#inputFileName='C:/Yingming Fang/project/Python/gitPython/job.properties'
#outputFileName='C:/Yingming Fang/project/Python/gitPython/system.indexes.json'
inputFileName=sys.argv[1]
outputFileName=sys.argv[2]
print inputFileName
#print outputFileName
'''
keywords B13keyColumns;B13relation
'''
def linevalidate(line,keywords):
	if line.find(keywords)==-1:
		return False
	else:
		return True
'''
sampe:B9relation=histScenarioListUi${diffSplitSymbol}histScenarioUi${diffSplitSymbol}exposureHistoricalStrategyUi
sepFirst:=
sepSecond:$
sepThird:}
extractRelation(line,'=','$','}')
'''
def extractRelationAndKeys(line,sepFirst,sepSecond,sepThird):
	relations=[]
	start=line.find(sepFirst)+1
	index=0
	while index!=-1:
		index =line.find(sepSecond,start)
		relations.append(line[start:index])

		index = line.find(sepThird,index)
		if index==-1:
			break
		else:
			index = index+1
			start = index
#	relations.append(line[start:len(line)])
	return relations

'''
	version:1
	database:c1_v5.
'''
def initialRecord(version,database):
	record={}
	record['v']=version
	record['key']={}
	record['ns']=database
	record['name']=''
	return record

input = open(inputFileName,'Ur')
outFile = open(outputFileName,'w+')
lines =input.readlines()
#print len(lines)
for i in range(len(lines)):
#	print i;
	if linevalidate(lines[i],'relation')==False:
		continue
	else:
#		print lines[i]
		relationLine = lines[i]
		relation = extractRelationAndKeys(relationLine,'=','$','}')
#		print "relation:%s" %(relation)
		i=i+1
		keysLine=lines[i]
#		print lines[i]
		keyColumn = extractRelationAndKeys(keysLine,'=','$','}')
#		print "keyColumn:%s" %(keyColumn)
		for j in range(len(relation)):
			out = initialRecord(1,'c1_v5')
			key={}
			ns=out['ns']
			name=""
			keysCell = keyColumn[j].split(',')
			for k in range(len(keysCell)):
				key[keysCell[k]]=1
				name +=keysCell[k]+"_1_"
			out['key']=key
			ns = ns+'.'+relation[j]
			out['ns']=ns
			name = name[0:len(name)-1]
			out['name']=name
#			print json.dumps(out)
			outFile.write(json.dumps(out))
			outFile.write('\n')

input.close()
outFile.close()









