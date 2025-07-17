a=[1,2,3,4,5,1,1,6,7]
b=[3,3,7,5,3,4,9,0,1]

#INSERTION
a.insert(0 , "Hi coders")
print(a)

#REMOVE
a.remove(3)
print(a)

#DELETION
popped = a.pop(0)
print(popped)
print(a)

#CLEAR
#a.clear()
#print(a)

#INDEX
index=a.index(2)
print(index)
print(a)

#COUNTER
counter = a.count(1)
print(counter)

#SORT IN ASCENDING
a.sort()
print(a)

#REVERSE
a.reverse()
print(a)

#PYTHON
copy=a.copy()
print(a)

#MINIMUM
minimum=min(a)
print(minimum)
print(max(a))

#SET
s1 = set(a)
s2 = set(b)
s3 = s1.intersection(s2)
print(list(s3))

#NESTED LIST
c=[2,4,6,a,[6,6,7]]

#RANGE
number = list(range(1,10,1))
print(number)

 #LIST COMPREHENSION
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares) 

squaresListCompre = [i ** 2 for i in range(1 , 11) if i % 2 == 0]
print(squaresListCompre)







