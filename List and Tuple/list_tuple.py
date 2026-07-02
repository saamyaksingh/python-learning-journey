'''
color= ["red","blue","green"]
num =[1,2,3,4,5]
length = len(num)
print(length)
print(color)
print(num)
a = sum(num)
b = max(num)
c = min(num)
print(a)
print(b)
print(c)
num.append(8)
print(num)

num.insert(3,17)
print(num)

num.pop(2)
print(num)

num.remove(1)
print(num)

num.clear()
print(num)

# del color
# print(color)

li = ("Rohan","Sohan","Mani")
print(type(li))
'''
#Question 1
'''
numbers = [10, 25, 7, 89, 45]
print(max(numbers))
'''
#Question 2
'''
numbers = [5, 10, 15, 20]
print(sum(numbers))
'''
#Question 3
'''
numbers = [1, 2, 3, 2, 4, 1, 5]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)
'''
#Question 4
'''
data = [10, 20, 30, 40, 50]
data.reverse()
print(data)
'''
#Question 5
'''
numbers = [2, 5, 2, 8, 2, 10]
print("2 =",numbers.count(2))
print("5 =",numbers.count(5))
print("8 =",numbers.count(8))
print("10 =",numbers.count(10))
'''
#Question 6
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for i in numbers:
    if i%2==0:
        print(i,"Even Number")
for i in numbers:
    if i%2!=0:
        print(i,"odd number")
'''
#Question 7
'''
list1 = [1, 2, 3]
list1.extend([4, 5, 6])
print(list1)
'''
#Question 8
'''
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)
'''
#Tuple
#Question 1
'''
numbers = (10, 20, 30, 40, 50)
print(numbers)
'''
#Question 2
'''
data = ("Python", "Java", "C++", "JavaScript")
length=len(data)
print(length)
'''
#Question 3
'''
fruits = ("Apple", "Banana", "Mango", "Orange")
first= fruits[0]
last= fruits[3]
print(first,last)
'''
#question 4
'''
numbers = (1, 2, 3, 2, 4, 2, 5)
a,b,c,d,e=0,0,0,0,0
for i in numbers:
    if i==1:
        a=a+1
    elif i==2:
        b=b+1
    
    elif i==3:
        c=c+1
    
    elif i==4:
        d=d+1
    elif i==5:
        e=e+1
print("1: ",a)
print("2: ",b)
print("3: ",c)
print("4: ",d)
print("5: ",e)
'''    
#Question 5
'''
colors = ("Red", "Green", "Blue", "Yellow")
for i in colors:
    print(colors.index(i))
'''
#Question 6
'''
data = (10, 20, 30, 40)
list=list(data)
print(list)
'''
#Question 7
'''
numbers = (45, 12, 89, 34, 67)
print("Minimum =",min(numbers),"Maximum =",max(numbers))
'''
#Question 8
'''
tuple1=(1,2,3)
tuple2=(4,5,6)
ok=tuple1+tuple2
print(ok)
'''
#Question 9
'''
names = ("Ali", "John", "David", "Emma")
print(type(names))
'''
#Question 10
'''
student = ("Abhishek", 22, "Python")
print("name:",student[0])
print("age:",student[1])
print("course:",student[2])
'''
#Question 11
'''
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)
'''
#Question 12
'''
numbers = (5, 10, 15, 20)
print(sum(numbers))
'''
#Question 13 Using Nested Loop
'''
data=((1, 2), (3, 4), (5, 6))
for i in data:
    for j in i:
        print(j)
'''
#Question 13 Using Indexing
'''
data=((1, 2), (3, 4), (5, 6))
print(data[0][0],data[0][1],data[1][0],data[1][1],data[2][0],data[2][1])
'''
#Question 14
'''
numbers = (1, 2, 3, 2, 4, 1, 5)
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)
'''
#Question 15
'''
numbers = (50, 10, 40, 20, 30)
ok=list(numbers)
ok.sort()
print(ok)
'''
