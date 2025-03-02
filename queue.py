# Elements in queue are first in first out 

# Using list as a queue \

stock_price_queue = []

stock_price_queue.insert(0,123)
stock_price_queue.insert(0,123.1)
stock_price_queue.insert(0,123.2)

print(stock_price_queue)

stock_price_queue.pop()

print(stock_price_queue)

# Not very efficent, thats why use deque from collections 

from collections import deque
q = deque()

q.append(8)
q.append(9)
q.append(10)
print(q)

q.pop()

print(q)


from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

pq.size()

pq.dequeue()