int={1,2,3,4,5,6,6}
print(int)
int.discard(4)
print(int)

real={7,6,8,9}
#union
print(int|real)
#intersection
print(int & real)
#difference
print(int - real)
#symmetric differene
#uncommon element
print(int ^ real)
#list to set
integers=[1,2,3,4,5,6,4,5,6,7,1]

q=set(integers)
print(q)
p=tuple(integers)
print(p)
