def containsNearbyDuplicate( nums, k) : 
    window = set() # window is the range of abs(i-j)<= k    
    l = 0  ## tracks the window left side  

    for r in range(len(nums)):
        # if exceed the range 
        if r - l > k : 
            window.remove(nums[l]) #remove first left element
            l+=1 # decrease the left side of the window
        if nums[r] in window:
            return True 
        window.add(nums[r])
    return False

def containsNearbyDuplicate_v2( nums, k) : 
    # space o(n)
    # time o(n)
    map = {}
    for i in range(len(nums)): 
        if nums[i] in map.keys(): 
            if i - map[nums[i]] <= k :
                return True 
        map[nums[i]] = i 
    return False

## think about it - try to improve it 
def containsNearbyDuplicate_v3( nums, k):
    
    n = len(nums)
    left , right = 0, 1
    while left < n-1:
        if nums[left] == nums[right] : 
            return True 
        right += 1
        if right == n or right-left > k: 
            left += 1
            right = left + 1
        
    return False
# nums = [1,2,3,1]
# nums = [1,2,3,1,2,3]
# nums = [1,0,1,1]
nums = [99,99]

# k = 1
# k = 12
# k = 3
k = 2

print('original ' , containsNearbyDuplicate(nums, k))
print('v3 ' ,  containsNearbyDuplicate_v3(nums, k))