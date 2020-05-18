a = [1,5,4,6,8,11,3,12]
even = list(filter(lambda x: (x%2 == 0), a))
print(even)

third = list(filter(lambda x: (x%3 == 0), a))
print(third)

b = [[0,1,8],[7,2,2],[5,3,10],[1,4,5]]
b.sort(key = lambda x: x[2])
print(b)


b.sort(key = lambda x: x[0]+x[1])
print(b)
