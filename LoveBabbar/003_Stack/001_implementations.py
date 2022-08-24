
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
            self.top -=1
    
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

if __name__ == '__main__':
    
    st = stack(10)
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(6)
    st.push(7)
    st.printStack()
    st.pop()
    st.pop()
    st.printStack()
    
    