#for variable_name in range(starting value,ending value,steps):
#  Code

for i in range(1,6,2):
    print(i)


name = 1225
for fn in name:
    print(fn)


for i in range(2,20+1,2):
    print(i)


for i in range(1,20+1,2):
    print(i)


for j in range(1,10+1):
    print(j)


for bgmi in range(10+1):
    print(bgmi)


for ff in range(1,10+1):
    print(ff,"=",ff*ff)


for jj in range(10,300+1,10):
    print(jj)


for i in range(1,13):  
    print(6*i,7*i,end=" ")


a=int(input("Enter Number"))
for j in range(1,10+1):
    print(a,"*",j,"=",a*j)


check=0
a=int(input("Enter Your Number"))
for i in range(2,a):
    if a%i==0:
        check=1
if check==1:
     print("not a prime number")
else:
     print("Prime")
 

sum=0
a=(input("Enter Digits"))
for i in a:
    sum= sum + int(i)
print (sum)


flag=0
a=(input("Enter your number:"))
for i in a:
    flag=flag+1
print(flag)


count=0

n=int(input("Enter a num"))
for i in range(1,n+1):
    if n>0:
        count=count+1
    n=n//10
print(count)


reverse=""
a=(input("Enter Your Number:"))
for i in a:
    reverse=i+reverse
print(reverse)


sum=1
a=(input("Enter Digits"))
for i in a:
    sum= sum * int(i)
print (sum)


c=0
b=1
e=0
a=int(input("Enter Term:"))
for i in range(1,a):
    print(c)
    e=c+b
    c=b
    b=e

