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

print("Print Alphabets and Letters pattern in python ")
lastNumber = 6
asciiNumber = 65
for i in range(0, lastNumber):
    for j in range(0, i+1):
        character  = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber+=1
    print(" ")
'''
    Print Alphabets and Letters pattern in python 
    A  
    B C  
    D E F  
    G H I J  
    K L M N O  
    P Q R S T U
'''
print("$$$$$$$$$$$$$$$$$$$$$$$$$")

decr = 8
count = 64
val = 65
for i in range(0, 5):
    for k in range(0, decr):
        print(end=" ")
    for j in range(0, i+1):
        count = count + 1
    val = count
    temp = val
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val - 1
    val = temp
    decr = decr - 2
    print()
 
