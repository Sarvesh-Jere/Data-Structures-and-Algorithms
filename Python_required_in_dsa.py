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

# Dont initialise the result to 0 before the loop when dealing with negative numbers, use res = max(nums)

res = max(nums)

# Dynamic Programming (DP) is a technique used to solve problems efficiently by breaking them down into smaller overlapping subproblems and 
# solving each only once while storing the results for reuse.
# For example in the below code, we mentioned two values - min_curr and max_curr to break down the problem 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_min,curr_max = 1, 1

        for n in nums:
            if n == 0:
                curr_min,curr_max = 1, 1
                continue
            tmp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)
            res = max(res, curr_max)
        return res

# Instead of recalculating every subarray’s product, 
# we dynamically update the maximum and minimum products at each step using previous results, 
# making the solution efficient (O(n) time complexity) and avoiding redundant work.

# Now we use the sliding window approach for sub strings

#To find non duplicate values instantly we can use set

# The length of a substring is calculated as - 


substring length = endind index - starting index + 1

# The sliding window technique is often used to solve problems that involve subarrays or substrings of a contiguous sequence. 
# It works by maintaining a window (a subarray or substring) that expands or contracts depending on the condition you're trying to satisfy.

#In this case, we are maintaining a window of unique characters from the string.
#  The window is defined by two pointers: l (left pointer) and r (right pointer). 
# The window expands as r moves forward, and if a duplicate character is found, the left pointer l moves forward to eliminate duplicates.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1 
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 

# When given an interval of array, sort it based on the start value, imagine we visualise it into a number line

#The expression below is a sorting key function, which ensures that intervals are sorted by their first element (the start time) in an interval while sorting
key=lambda i: i[0]

# for example 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])





# output[-1] gives us the last interval, which is a list.
#output[-1][1] accesses index 1 of that list, which is the end time of the last interval.
# ex - output = [[1, 6], [8, 10], [15, 18]]
# this will give 18

# Now given below is an example to solve a problem using left and right pointer 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r = r+1
        return maxProfit

# Now on to a graph problem 
 # Algorithm commonly used - 

1 DFS - 
Data structures used - Hashset or stack, uses pop, also uses hashmap(dict)

2 BFS - 
Data structures used - Queue(double ended) and Hashset to detect duplicate nodes so we dont get stuck in a loop, uses popleft
also uses Hashmap(dict)

3 Union find
Used to combine togather disjoint sets 

4 Topological Graph 
A type of DFS where we have an directed acyclic graph 
Hashset

5 Dijikstra shortest path algorithm 
Heap or priority queue and hashset

# Coding in graph - 
 len(grid) gives the number of rows.
len(grid[0]) gives the number of columns, which is used to navigate and manage the grid's structure.

# to check an element and see if its 1 in a graph where r and c are used in for loop 
if grid[r][c] == "1":

# In your code you need to initialise bfs in the follwoing , you will also have to use queue 
def bfs(start, graph):
    queue = collections.deque()
    visited = set()
    
    queue.append(start)
    visited.add(start)

    while
# and then of course write a while loop ahead of it 

# Now we see how to use a depth first search in a graph problem 

# In all recurrsive function, we first look at the base cases 

# Also in DFS understand the difference between recurrsive and iterative 

#recurssive - Recursive DFS (Using Function Calls)
We let Python's function calls handle the "stack" for us.
Each function call goes deeper into the graph, and once there are no more neighbors, it "backtracks" automatically.


# Iterative - 
Iterative DFS (Using a Stack Manually)
Instead of relying on function calls, we use a stack to track what to explore next.
We manually push and pop nodes like a "to-do" list.

# Recurrsive DFS - Most common syntax
def dfs(node, graph, visited):
    if node in visited:  # If already visited, return
        return
    visited.add(node)  # Mark node as visited
    print(node)  # Process node (e.g., print or store result)
    
    for neighbor in graph[node]:  # Explore all neighbors
        dfs(neighbor, graph, visited)  # Recursive call

# Driver code
visited = set()
dfs('A', graph, visited)

# Clone graph meaning in a graph problem - 
# To create a clone of a graph with samw nodes, use hashmap oldtoNew = {} to track

# Now onto trees 
left, right = dfs(root.left), dfs(root.right)

# Used in trees , this  line calls the dfs function recursively on the left child (root.left) and the right child (root.right) of the current node (root).

# Valid Binary searh tree - A valid binary search tree (BST) is a binary tree that satisfies the BST property, which states that:

#The left subtree of a node contains only nodes with values less than the node’s value.
#The right subtree of a node contains only nodes with values greater than the node’s value.
#Both the left and right subtrees must also be binary search trees (i.e., the BST property holds recursively for all nodes).

In the TreeNode class, .val is an instance attribute that stores the value of the node.

used in the below code of a sum 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True 

            if not(node.val < right and node.val > left):
                return False 

            return (valid(node.left, left, node.val) and valid(node.right,node.val , right))

        return valid(root, float("-inf"),float("inf"))

