#Nested list
rohit=["Happy","Monica",2,'r',[3,6],7,"digit","welcome to my house"]
print(rohit[1][3])
print(rohit[5])
print(rohit[4][1])
#Negative indexing
print(rohit[-1][-5])
print(rohit[-2][1])
#slicing
my_list1=['p','r','o','m','m','i','n','g']
print(my_list1[:-3])
print(my_list1[2:2])
print(my_list1[2:5])
print(my_list1[-6:3])
#change elements in LISTS
odd=[2,4,6,8,"its even",10,12]
odd[0]=1
print(odd)
odd[1:3]=[3,5]
print(odd[1:5])
#add one item-APPEND-in last
#add seveeral items -EXTEND-in last
#APPEND
odd.append(11000)
odd.append([11,45])
print(odd)
#EXTEND
odd.extend([112,114,116])
print(odd)
#+ = concatenation - it do not edit original list||
print(odd + ["rock"])
# *
print(odd * 2)
#INSERT - one item at desired location and by using slicing we can add more items.
b=[1,0,7,4]
b.insert(2,3)
print(b)
b[3:3]=[9,88,56,87]
print(b)

#del - to delete elements or entire list
p=['p', 'o', 'r','l', 'b','bhaskar','bc']
del p[3]
print(p)
del p[2:4]
print(p)
#pop() -index,to remove an item - use as stack FILO -no index,last
#remove() - we give item which we want to remove
#clear() - to empty a list
p.remove('o')
print(p)
p.pop(0)
print(p)
p.pop()
print(p)
p.clear()
print(p)
#index
my_list=[3,8,1,6,0,8,4]
print(my_list.index(0))
#count
print(my_list.count(8))
#sort
my_list.sort()
print(my_list)
#reverse
my_list.reverse()
print(my_list)
'''
list comprehension{List comprehension is an elegant and concise way to create new list from an existing list in Python.
List comprehension consists of an expression followed by for statement inside square brackets.
Here is an example to make a list with each item being increasing power of 2.}
'''
po2=[2**x for x in range(10)]
print(po2)

#list membership
print('p' in my_list)
print(8 in my_list)
print('o' not in my_list)

























