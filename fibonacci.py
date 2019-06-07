n=int(input("enter the number of items"))
def fibonacci(n):
    if(n<2):
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
for i in range(n):
    print("Fibonacci(",i,")=",fibonacci(i))
