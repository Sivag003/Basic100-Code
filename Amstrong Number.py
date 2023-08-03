n=int(input("Enter the Number: "))
temp=n
base=len(str(n))
ams=0
while(temp>0):
  rem=temp%10
  ams=ams+(rem**base)
  temp=temp//10
if(ams==n):
  print("The given number is Amstrong!!")
else:
  print("The given number is not a Amstrong")
