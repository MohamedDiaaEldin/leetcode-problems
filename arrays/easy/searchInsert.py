def searchInsert(nums, target):
    low, high = 0, len(nums) -1 
    while low <= high : 
        mid = (low + high) // 2 
        if nums[mid] == target : 
            return mid 
        elif  target < nums[mid]  : 
            high = mid - 1 
        else: 
            low = mid + 1
    return low

nums = [1,3,5,6]
print(searchInsert(nums, 7))
