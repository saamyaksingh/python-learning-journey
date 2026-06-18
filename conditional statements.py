'''
a=int(input("Enter Number:"))
if a%5==0:
    print("hello")
else:
    print("bye")
'''
'''
bill=0
Unit=int(input("Enter Units:"))
if Unit<=100:
    print("no charge")
elif Unit>100 and Unit<=200:
    bill=(Unit-100)*5
    print(bill)
else:
    bill=500 + (Unit-200) *10
    print(bill)
'''
'''
a=(int)(input("Cost price of Bike"))
rt=0

if a<=50000:
    rt=(a*5)//100
    print(rt)
elif a>50000 and a<=100000:
    rt=a*0.1
    print(rt)
else:
    rt=a*0.15
    print(rt)
'''
'''
a=int(input("your number"))
if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==4:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Invalid Input")
'''

'''
a=input("city")
if a==("delhi"):
    print("red fort")
elif a==("agra"):
    print("taj mahal")
elif a==("jaipur"):
    print("jal mahal")
else:
    print("Invalid Input")
'''
'''
a=int(input("Enter Your Age:"))
if a>=60:
    print("You are a Senior Citizen")
else:
    print("You Are Not a Senior Citizen")
'''
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if a<b:
    print(a)
elif a>b:
    print(b)
'''
'''
net=0
a=int(input("Enter Your Sallary"))
b=int(input("Years of Service"))
if b<6:
    net=a*0.05
    print(net)
elif b>=6 and b<=10:
    net=a*0.08
    print(net)
else:
    net=a*0.1
    print(net)
    '''
'''
a=int(input("Total Number Of Working Days:"))
b=int(input("Total number of days for absent:"))
present=a-b
percentage=(present/a)*100

if percentage<75:
    print("You are not eligible to sit in exam")
else:
    print("You are eligible to sit in exam")
'''
'''
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=input("Enter Opreator")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Invalid Input")
'''
'''
wage=0
a=int(input("Enter Your Age:"))
b=(input("Enter Your Gender:"))
c=int(input("Enter Days You Want To Work:"))
if a>=18 and a<30 and b=="m":
    wage=c*700
    print(wage)
elif a>=18 and a<30 and b=="f":
    wage=c*750
    print(wage)
elif a>30 and a<=40 and b=="m":
    wage=c*800
    print(wage)
elif a>30 and a<=40 and b=="f":
    wage=c*850
    print(wage)
else:
    print("Invalid Input")
'''
