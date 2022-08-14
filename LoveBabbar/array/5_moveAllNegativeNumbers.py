#Move all negative numbers to beginning and positive to end with constant extra space

a = [-12, 11, -13, -7, 6, 5, -13, 8, -6, 9 ,10 ]
n = len(a)

j = 0
for i in range(n):
    if a[i]<0:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j += 1
print(a)