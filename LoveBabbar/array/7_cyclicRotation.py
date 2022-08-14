# cyclic rotate array by k elements in clockwise direction
a = [1,2,3,4,5,6,7,8,9]
#output = [6,7,8,9,1,2,3,4,5]
k = 4
n = len(a)
print(a)
l1 = a[0:n-k]
l2 = a[n-k:]
a = l2 + l1
print(a)
