import operator
a=[3,2,5,1,4]
# sorted():this method will not impact the origin array
#b=sorted(a,reverse=True)
#list.sort(): will not impact the origin array
#b = a.sort(reverse=True)
def data_comp(a,b):
	if a < b :
		return -1
	elif a==b:
		return 0
	else:
		return 1
#customized sort method will not also impact the result
#b= a.sort(cmp=data_comp)
#b=sorted(a,cmp=data_comp)
#summary: sorted() will have a return value and don't impact the origin array, however,
#the list.sort() will impact the origin array


a={1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
b = sorted(a,reverse=True)
b =sorted("This is a test string from Andrew".split(), key=str.lower)
#print a
#print b

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

b = sorted(student_tuples, key=lambda ins:ins[2])

b = sorted(student_tuples, key=operator.itemgetter(2))
#print b
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

c=sorted(student_objects,key=lambda ins: ins.age)
c=sorted(student_objects,key=operator.attrgetter('age'))

print c