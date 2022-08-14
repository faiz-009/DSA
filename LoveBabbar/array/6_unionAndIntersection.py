#return union and intersection of two arrays

a = [2,3,4,51,234,64,8,43,75465,43,886,3,0,9,6]
b = [8, 9,897,786, 44,9,34,0,5]

print("A list := ",a)
print("B list := ",b)

a = set(a)
b = set(b)

print("A set := ",a)
print("B set := ",b)

c = a.union(b)
print("union of a and b := ",c)
c = a.intersection(b)
print("a intersection b := ",c)