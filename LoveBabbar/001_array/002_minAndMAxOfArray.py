'''
Maximum and minimum of an array using minimum number of comparisons

Difficulty Level : Easy
Write a C function to return minimum and maximum in an array. Your program should make the minimum number of comparisons. 
'''

# a = [4,6,7,8,9,10,35,2,0,6,24,4]
a = [-1, 3,5]
n = len(a)

#if there exists only one element
min = a[0]
max = a[0]

if n !=1 :
    for i in range(1, n):
        if a[i]<min:
            min = a[i]
        elif a[i]>max:
            max = a[i]

print("Min :- ", min)
print("Max :- ", max)


