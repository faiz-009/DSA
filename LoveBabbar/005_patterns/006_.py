'''
12345
1234
123
12
1

'''
n = int(input("Enter size: "))

for i in range(n+1):
    for j in range(1, n+1-i):
        print(j, end='')
    print()
