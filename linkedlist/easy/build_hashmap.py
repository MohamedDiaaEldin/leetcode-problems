'''
706. Design HashMap
Solved
Easy
Topics
Companies
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
'''

# it doesn't work because of hash function 
# collision problem 
class MyHashMap(object):
    def __init__(self):
        self.array_size = 10 ** 6
        self.map = [None] * self.array_size
    def hash(self, key):
        str_key = str(key)
        hash_value = 0

        for char in str_key:
            hash_value += (hash_value << 5) - hash_value + ord(char) * 100 
        index = hash_value % self.array_size
        return index
    # o(1)
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hashed_key = self.hash(key)
        self.map[hashed_key] = value

    # o(1)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hashed_key = self.hash(key)
        if self.map[hashed_key]:                        
            return self.map[hashed_key]
        else :
            return -1 

    # o(1)
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashed_key = self.hash(key)
        self.map[hashed_key] = None

# it works will 
class MyHashMap_v1(object):

    class ListNode():
        def __init__(self, index, value):
            self.index = index
            self.value = value

    def __init__(self):
        self.map = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # o(n)
        for i in range(len(self.map)): 
            if self.map[i].index == key : 
                self.map[i].value = value
                return;
        self.map.append( self.ListNode(key, value))
        

    # o(n)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.map)): 
            if self.map[i].index == key : 
                return self.map[i].value 
        return -1 

    

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # o(n)
        for i in range(len(self.map)): 
            if self.map[i].index == key : 
                self.map.remove(self.map[i]) 
                return 


