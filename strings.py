chell='keep the blue flag flying high'
print(chell.__len__())
print(chell.index('b'))
print(chell.count('f'))
#slicing
print(chell[0:4])
print(chell[::-1])
print(chell.upper())
#repetition
print(chell*2)
print(chell+'lampard')
if 'k' in chell:
    print('it is an element')
if 'z' not in chell:
    print('it is not an element')
