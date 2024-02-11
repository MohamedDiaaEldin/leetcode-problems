'''
136. Single Number
Solved
Easy
Topics
Companies
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''
def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # using Xor operator 
    unique = 0 
    for num in nums : 
        unique ^= num
    return unique



# using a set
# O(n) time
# O(n) space
def singleNumber_v2( nums):
    ##############
    s = set()
    for num in nums : 
        if num in s  : 
            s.remove(num)
        else : 
            s.add(num)
    return next(iter(s))


# using a hash map
# O(n) + o(n) = o(n) time
# O(n) space        
def singleNumber_v3( nums):
    map = {}
    for num in nums : 
        if num in map.keys(): 
            map[num] += 1
        else :
            map[num] = 1
    for key in map.keys(): 
        if map[key] == 1 : 
            return key
        

        
        