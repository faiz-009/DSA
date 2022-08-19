a = [4,6,7,8,9,10,35,2,0,6,24,54]
n = len(a)


#if there exists only one element
min=0
max=0
if n ==1 :
    min = a[0]
    max = a[0]
else:
    min = a[0]
    max = a[0]
    i = 1
    while i<n:
        if a[i]<min:
            min = a[i]
        elif a[i] > max :
            max = a[i]
print("Min :- ", min)
print("Max :- ", max)