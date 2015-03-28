def Sum5(number1,number2,number3,number4,number5):
    result=number1+number2+number3+number4+number5
    print result
                                   
number1=input("Put number1")
number2=input("Put number2")
number3=input("Put number3")
number4=input("Put number4")
number5=input("Put number5")

def Sum5improved(number1,number2,number3,number4,number5):
    result=number1+number2+number3+number4+number5
    print result
                                   
(number1,number2,number3,number4,number5)=input("Put 5 numbers with ' , ')")

Sum5improved(number1,number2,number3,number4,number5)


def value(x):
    a= float (x)
    b= int (x)
    print "The Integer value for", x, "is", b, "and the float is ",a
    
number=input("Put the integer number :")

value(number)
def Biggest(number1,number2,number3,number4,number5):
    x=max(number1,number2,number3,number4,number5)
    print "The largest is",x                             


Biggest(number1,number2,number3,number4,number5)

def Smallest(number1,number2,number3,number4,number5):
    x=min(number1,number2,number3,number4,number5)
    print "The smallest is",x                             


Smallest(number1,number2,number3,number4,number5)

def Mean(number1,number2,number3,number4,number5):
    listo=[number1,number2,number3,number4,number5]
    devided=len(listo)
    summmary=sum(listo)
    result=summmary/float (devided)
    print "The mean is",result                             

Mean(number1,number2,number3,number4,number5)


def SumToN(N):
    result=sum( range (1,N+1) )
    print "Sum from 1 to N is :",result

N=input("Put N value : ")
SumToN(N)






def IsOdd(XY):
    bollean_IsOdd=bool(XY%2!=0)
    if bollean_IsOdd:
        print XY,"is odd"
    else:
        print XY,"is even"#extended version :)

XY=input("Put XY value : ")
IsOdd(XY)

def IsEven(XY):
    bollean_IsEven=bool(XY%2==0)
    if bollean_IsEven :
        print XY,"is even"

XY=input("Put XY value : ")
IsEven(XY)


def Medal (place):
    if place==1:
        print "gold"
    elif place==2:
            print "silver"
    elif place==3:
            print "brown"
    else:
            print "Ooops you don't have medal :("

place=input ("please provide us the place number:")
Medal(place)
    


def CheckRange(start,finish,step):
    for start in range(start,finish+1,step):
        print IsOdd(start)

start=input("Put start value : ")
finish=input("Put stop value : ")
step=input("Put step value : ")
CheckRange(start,finish,step)

