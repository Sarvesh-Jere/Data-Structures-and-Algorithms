# Process using python dictionary

stock_prices = {
    "AAPL": 189.54,
    "GOOGL": 2753.32,
    "AMZN": 142.18,
    "MSFT": 326.79,
    "TSLA": 243.15
}
# To find a particula stock price

print(stock_prices["TSLA"])

# Implementing hashmap to get values in O(1) complexity

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

print(get_hash("March 28"))

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None  

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420