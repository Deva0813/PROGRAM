# output of 4th ques
'''
import array
a = [1, 2, 3]

print(a[-3])
print(a[-2])
print(a[-1])
'''

#output of 5th ques
'''
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])
'''

# 6th progarm
'''
print (sum(range(1,101)))
'''

# 7th program
'''
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
     sum += 1
    if ls[1] == 'Bob':
     sum += 10
print (sum)
'''
#10 program
'''
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
'''

#11 program
'''
str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")
a=list(set(str1)&set(str2))
print("The common letters are:")
for i in a:
    print(i)
'''

#12 programs
'''
class Acc:
    def __init__(self, id):
        self.id = id
        id = 555

acc = Acc(111)
print (acc.id)
'''
#13
'''
for i in  range(2):
    print (i)
 
for i in range(4,6):
    print (i)
'''
#14
'''values = [1, 2, 3, 4]
numbers = set(values)
 
def checknums(num):
    if num in numbers:
        return True
    else:
        return False
 
for i in  filter(checknums, values):
    print (i)
'''
#15
'''counter = {}
 
def addToCounter(country):
    if country in  counter:
        counter[country] += 1
    else:
        counter[country] = 1
 
addToCounter('China')
addToCounter('Japan')
addToCounter('china')
 
print (len(counter))
'''
#16
'''
dictionary = {}
dictionary [1] = 1
dictionary ['1'] = 2
dictionary [1] += 1
  
sum = 0
for k in dictionary:
    sum += dictionary[k]
  
print (sum)
'''
#17
'''
lower = int(input("Enter the lower Interval No.: "))
upper = int(input("Enter the upper Interval No.: "))

for num in range(lower, upper+1):

    for x in range(2,num):
        if num%x==0:
            break
    else:
        print(num)
'''
#18
'''
x=int(input('Enter a integer: '))
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(x)
'''
#19
'''
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    el = int(input())
 
    lst.append(el)

a=int(input("Entre the Divisor value :"))

result = list(filter(lambda x: (x % a == 0), lst))

print("Numbers divisible by",a,"are",result)
'''
#20
import calendar
yy=int(input("Enter thhe year: "))
mm=int(input("Enter the month: "))
print(calendar.month(yy,mm))

