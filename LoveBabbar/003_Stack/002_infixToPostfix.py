
class stack:
    maxSize = 0
    top = -1
    stack = []
    
    def __init__(self, size):
        self.maxSize = size
    
    def push(self,x):
        if not self.isFull():
            self.top+=1
            self.stack.insert(self.top, x)
    
    def pop(self):
        if not self.isEmpty():
            x = s.stack[s.top]
            self.top -=1
        return x
    
    def isEmpty(self):
        if self.top == -1 : 
            return True
        else:
            return False
    
    def isFull(self):
        if self.top>self.maxSize:
            return True
        else:
            return False
        
    def printStack(self):
        
        for i in range(self.top+1):
            print(self.stack[i])
        print()
    
    def peek(self):
        return self.stack[self.top]

if __name__ == '__main__':
    
    arr = input("Enter the arr: ")
    opr = ['+', '-', '*', '/']
    dict = {'+':1, '-':1, '*':2, '/':2}
    n = len(arr)
    s = stack(n)
    
    ans = ''
    
    for i in range(n):
        if arr[i] not in opr:
            ans += arr[i]
        else:
            if s.top == -1 :
                s.push(arr[i])
            elif dict[s.stack[s.top]] < dict[arr[i]]:
                s.push(arr[i])
            else:
                while not (s.stack[s.top] <arr[i]) or s.top != -1:
                    ans += s.pop()
                s.push(arr[i])
                    
                
    while not s.isEmpty():
        ans += s.pop()
    
    print(ans)
                
                                
                
    
    