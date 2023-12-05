## brute force solution
## O(N^2) time 
## O(1) Memory
def two_sum(nums, target): 
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            if nums[i] + nums[j] : 
                return [i, j]
    
## O(N) time 
## O(N) memory
def twoSum( nums, target):
    if len(nums) < 2 : 
        return None
    # maps each number to it's index
    num_index = {}
    for i in range(len(nums)):
        complemented = target - nums[i] 
        if complemented in num_index : 
            return [i, num_index[complemented] ] 
        else:
            num_index[nums[i]] = i 
    

def twoSum_v2(nums, target): 
    nums_index = sorted(enumerate(nums), key= lambda x: x[1])
    left=0 
    right=len(nums)-1
    while left < right :
        sum = nums_index[left][1] + nums_index[right][1]
        if sum == target : 
            return [nums_index[left][0], nums_index[right][0]]
        elif sum > target :
            right -= 1
        else:
            left += 1
    return []


nums = [2,7,11,15]
target = 9 

# print(twoSum(nums, target))
# print(two_sum(nums, target))
print(twoSum_v2(nums, target))
