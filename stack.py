s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

s.pop()
print(s)

#Here we have usd the stack logic which is last in first out to store the website urls in a list and then used pop to access the last element which was in

# Use the below method to access the last elemnt without removing it from the list 

s[-1]
print(s)

'''
The issue with using a list as a stack is that list uses dymanic array internally and when it reaches its capacity it will reallocate a big chunk of memory somewhere 
else in memory area and copy all the elements. 
For example in below diagram if a list has a capacity of 10 and we try to insert 11th element, 
it will not allocate new memory in a different memory region, copy all 10 elements and then insert the 11th element. 
So overhead here is (1) allocate new memory plus (2) copy all existing elements in new memory area
'''

# Therefore we use dequeue which is a generalisation of stack and queue as a stack
# using deque as a stack
from collections import deque
stack = deque()

'''
['__add__',
 '__bool__',
 '__class__',
 '__contains__',
 '__copy__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'appendleft',
 'clear',
 'copy',
 'count',
 'extend',
 'extendleft',
 'index',
 'insert',
 'maxlen',
 'pop',
 'popleft',
 'remove',
 'reverse',
 'rotate']
'''

#all these above methodswe can use for deque as a stack

stack.append("https://www.cnn.com/")
print(stack)


