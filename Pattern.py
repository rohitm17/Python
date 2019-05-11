for i in range(1,6):
    print()
    for j in range(1,i+1):
        print('#',end='')

'''
#
##
###
####
#####
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end='')

'''
1
12
123
1234
12345
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i,end='')
'''
1
22
333
4444
55555
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

count=0
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(count,end='')
        count=count+1
'''
0
12
345
6789
1011121314
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
    1
   12
  123
 1234
12345
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end='')
    for l in range(i-1,0,-1):
        print(l,end='')
    print()

'''
    1
   121
  12321
 1234321
123454321
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print(i,end='')
    print()
'''
    1
   22
  333
 4444
55555
'''
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

