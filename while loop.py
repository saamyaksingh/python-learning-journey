#question 1
#a
'''
i=1
while i<=10:
    print(i*2)
    i=i+1
'''
#b
'''
i=1
while i<=10:
    print(i*2-1)
    i=i+1
'''
#c
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
#d
'''
i=0
while i<=9:
    print(i)
    i+=1
'''
#question 2
'''
i=1
while i<=10:
    print(i*i)
    i+=1
'''
#question 3
'''
i=10
while i<=300:
    print(i)
    i+=10
'''
#question 4
'''
i=1
while i<=10:
    print(6*i,7*i,end=" ")
    i+=1
'''
#question 5
'''
total=0
i=1
while i<=10:
    total=total+i
    i+=1
print("Sum =",total)
'''
#question 6
'''
a=int(input("Enter Number"))
i=1
while i<=10:
    print(a*i)
    i+=1
'''
#question 7
'''
check=0
a=int(input("Enter Number:"))
i=2
while i<a:
    if a%i==0:
        check=1
    i+=1
if check==1:
    print("Not a Prime Number")
else:
    print("Prime")
'''
#question 8
'''
sum = 0
a = int(input("Enter Number: "))

while a > 0:
    digit = a % 10
    sum = sum + digit
    a = a // 10

print("Sum =", sum)
'''
#question 9
'''
count = 0
a = int(input("Enter Number: "))

while a > 0:
    count = count + 1
    a = a // 10

print("Number of Digits =", count)
'''
#question 10
'''
a = int(input("Enter Number: "))

reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

print("Reverse =", reverse)
'''
#question 11
'''
product = 1
a = int(input("Enter Number: "))

while a > 0:
    digit = a % 10
    product = product * digit
    a = a // 10

print(product)
'''
#question 12
'''
n = int(input("Enter Number of Terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count = count + 1
'''
#question 13
'''
a = int(input("Enter Number: "))

fact = 1
i = 1

while i <= a:
    fact = fact * i
    i = i + 1

print(fact)
'''
#question 14
'''
n = int(input("Enter Terms: "))

num = 0
i = 1

while i <= n:
    num = num * 10 + 2
    print(num)
    i = i + 1
'''
#question 15
'''
n = int(input("Enter Terms: "))

i = 1

while i <= n:
    print(i * i)
    i = i + 1
'''
#question 17
'''
a = "PYTHON"

i = 0

while i < 6:
    print(a[i])
    i = i + 1
'''
#question 18
'''
i = 1

while i <= 49:
    print(i, "----", 50 - i)
    i = i + 1
'''
#question 19
'''
n = int(input("Enter Terms: "))

i = 1
total = 0

while i <= n:
    total = total + i**3
    i = i + 1

print(total)
'''