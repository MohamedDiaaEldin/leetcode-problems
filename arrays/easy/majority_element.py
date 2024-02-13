'''
169. Majority Element
Solved
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?

'''
def majorityElement( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ## boyer moore algorithm  - simple implementation
    count , majority = 0, 0
    for n in nums : 
        if count == 0 : 
            majority = n
        count += 1 if majority == n else -1 
    return majority


## boyer moore algorithm 
def majorityElement_v2( nums):
    majority = nums[0]
    count = 1
    for i in range(1, len(nums)): 
        if nums[i] == majority : 
            count += 1 
        elif count == 0 : 
            majority = nums[i]
            count = 1 
        else : 
            count -= 1 
        
    return majority


def majorityElement_v3( nums):
    if len(nums) == 1 :
        return nums[0] 
    map = {}
    for num in nums : 
        if num in map.keys(): 
            map[num] += 1 
            if map[num] > len(nums) // 2 : 
                return num           
        else : 
            map[num] = 1 
