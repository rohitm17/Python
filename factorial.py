n=int(input("enter the number"))
d=1
for i in range(0,n):
    d=d*n
    n=n-1
    
print(d)
 #or
while(n>1):
    d=d*n*(n-1)
    n=n-2
print(d)
