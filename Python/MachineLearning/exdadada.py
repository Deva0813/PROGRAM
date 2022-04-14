'''
str =["90","10","30","40"]
count =3
sum= 0
for i in [1,2,5,4]:
    s=str[count]
    sum=float(s)+i
    print(sum)
    count -=1
'''
'''
floatNumbers = []
n = int(input("Enter the list size : "))


for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

    print("User List is ", floatNumbers)
'''
'''
a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

    if a > 0 and b > 0 and c > 0:
        print("The numbers are greater than 0")
    else:
        print("Atleast one number is not greater than 0")
'''
'''
a = 10
  
if not a: 
    print("Boolean value of a is True") 
  
if not (a%3 == 0 or a%5 == 0): 
    print("10 is not divisible by either 3 or 5") 
else: 
    print("10 is divisible by either 3 or 5")
'''
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
    
print (lst)
'''
'''
n = int(input())
arr =map(int, input().split())
print(sorted(list(set(arr)))[-2])
'''
string = "Perfect, Plan B" 
L = string.split(',') 
print (L)
