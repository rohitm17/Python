#using while loop
x=int(input("enter the number :"))

temp=0

while(x>0):
      m=x%10
      temp=temp*10+m
      x=x//10
print(temp)
