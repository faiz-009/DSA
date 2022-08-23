# input: geeks
# output: g, 1
#         e, 2
#         k, 1
#         s, 1

s = input()
n = len(s)
ans = {}

for i in range(n):
    if s[i] not in ans:
        ans[s[i]] = 1
    else:
        a = ans[s[i]]
        ans[s[i]] = a+1
    
print(ans)

