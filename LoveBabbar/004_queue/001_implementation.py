
from multiprocessing import set_forkserver_preload


class myQueue:
    
    maxSize = 0
    front = -1
    rear = -1
    queue = []
    
    def __init__(self, size):
        self.maxSize = size
    
    def enqueue(self, x):
        if self.front==self.rear==-1:
            self.front+=1
            self.rear+=1
        elif self.rear < self.maxSize :
            self.rear +=1 
        
        self.queue.insert(self.rear, x)
            
    def dequeue(self):
        if self.front > -1:
            self.front +=1
    
    def printQueue(self):
        
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end=' ')
        print()
        
if __name__ == '__main__':
    q = myQueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(10)
    q.enqueue(40)
    q.enqueue(50)
    
    
    q.printQueue()
    
    q.dequeue()
    q.dequeue()
    
    q. printQueue()