num1=int(input("Enter the Numerator1:"))
den1=int(input("Enter the Denomenator1:"))
num2=int(input("Enter the Numerator2:"))
den2=int(input("Enter the Denomenator2:"))
def lcm(a,b):
    if(a==b):
        lc=a
    else:
        for i in range(max(a,b),1+(a*b),max(a,b)):
            if(i%a==0 and i%b==0):
                lc=i
    return lc
d=lcm(den1,den2)
print(d)
print("The sum of ",num1,"/",den1, "+",num2,"/",den2,"=",num1+num2,"/",d)
