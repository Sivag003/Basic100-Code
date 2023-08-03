m=int(input("Enter the no. of Mangoes:"))
n=int(input("Enter the no. of Persons:"))
def calculate(m,n):
    if(m<n):
        return 0
    ways=way(m+n-1,n-1)
    return ways
def way(m,n):
    a=fact(m)
    b=fact(n)
    c=fact(m-n)
    return a//(b*c)
def fact(f):
    if f== 0:
        return 1
    return f*fact(f-1)
    
print("No. of ways",calculate(m,n))

