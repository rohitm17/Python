#tuples-immutable
football=('hell','hell','lampard','rohit','nisha')
cricket=('rohitsh','eshank','ankit','anshal')
#indexing
print(football[1])
print(football.index('rohit'))
#slicing
print(football[0:2])
#concatenation
footcrick=football+cricket
print(footcrick)
#repetition
print(football*2)
#count
print(football.count('hell'))
#length
print(football.__len__())


foot=[('hell','hell','lampard','rohit','nisha'),('rohitsh','eshank','ankit','anshal')]
print(foot[1][1])


points=[(1,2),(3,4),(6,7)]
points.append((5,6))
print(points)
points.remove((1,2))
print(points)
