# To use for loop to read in reverse 

for i in range(5, 1, -1):
    print(i)

# Pass a third argument with negative one above

# Division is decimal by default

print(5/2)

# For rounding up to int use double 

print(5//2)

# Arrays called list in python are dynamic by default 

arr = [1,2,3]

print(arr)

# Array can be used as stack in python
arr.pop()
arr.append(4)

# can also insert in array 

arr.insert(1, 7)

print(arr)

# Loop through arrays 

nums = [1,2,3]

for i in range(len(nums)):
    print(nums[i])

# Without index

for i in nums:
    print(i)

# Use enumarate to give both index and value

for i, n in enumerate(nums):
    print(i, n)

# To do a custom sort of array, use lambda function, basically lambda is a function with no name
arr = ["Sarvesh", "Aditya", "Jane", "Doe"]
arr.sort(key =lambda x: len(x))

# Strings are similar to arrays, use double or single quotes to assign
s = "abc"
print(s[0:2])
# As seen above can slice similar to an array 
# But unlike array they are immutable, that means we cant modify ther value as we do for array, updating string creates a new string

print(str(123)+ str(123))

print(int("123") + int("123"))

# String and integers can be converted to each other 

# Hash sets 
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

# Of course cannot store any duplicates 

# HashMap aka dictonary, single most data structures that can be used 

myMap = {}

myMap["Sarvesh"] = 88
myMap["Prathamesh"] = 92

# This is how you write hashmap for dsa 

print(myMap)
print(len(myMap))

# Can also initialise the hash map, same as adding value to a hash map as shown above

yourMap = {"Sarvesh":88, "Prathamesh":92}
print(yourMap)

# Dict comprehension of hash  map, used frequently when doing graph problems

myMap = {i:2*i for i in range(3)}
print(myMap)

# Looping through maps 
myMap = {"Sarvesh" : 90, "Prathamesh" : 92}
for key in myMap:
    print(myMap[key])
# Alternatively use.items to unpack 

for key in myMap.items():
    print(key)

# You can also directly take out values 
for key in myMap.values():
    print(key)


# Python also has tuples , similar to arrays but use (), also immutable 
tup = (1,2,3)

# Mostly used as keys for hash maps or hash sets because lists cant be used as keys , for example below 
myMap = {(1,2) : 3}
print(myMap[(1,2)])


# Heaps 
# Used under the hood in arrays , like we create an empty array, by default in python heaps are minimum heaps 
import heapq
minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)

# Minimum is always at index 0 
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# We get values in smallest to largest since minHeap 

# while python technically doesnt have maxHeap, the way around is  using -1 while push and pop

while len(minHeap):
    print(-1 * heapq.heappop(minHeap))

# Toi build heap from initial values use heapify 
arr = [2,3,5,1,6]

heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# Functions use def to initialise

# Nested functions are used in coding interviews, specially in recurresion problem 

def outer(a,b):
    c= a +b

    def inner():
        return a + b + c
    return inner

print(outer('a','b'))

# Classes in python 
# CLass
class Myclass:
    #constructor 
    def __init__(self,num):
        #create member variables
        self.nums = nums
        self.size = len(nums)

    def getLength():
        self.len(nums)

# To get the index in the for loop iteration 

for i in range(len(nums)):

# To get the values in the for loop iteration

for i in nums:

# max() function returns largest of the values passed 

max_sum = max(max_sum, curr_sum)

# We can also write the range(len(nums)) within a range using below, says upto -1 and deceasing by value 1

for i in range(j, len(nums),-1,-1):


