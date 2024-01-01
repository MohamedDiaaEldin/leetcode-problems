'''
Solutions Notes 
remove_duplicates, remove_duplicates_v2 and remove_duplicates_v3 are using  the same approach
while remove_duplicates_v4 use different one witch uses more memory and doesn't remove elements in place 


Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}



'''


def removeDuplicates(nums):
    left = 0 
    for num in nums:
        if num > nums[left]: 
            left += 1
            nums[left] = num
    return left+1


# another solution with the same approach
def removeDuplicates_v2( nums) -> int:
    i,j=0,1
    while i<=j and j<len(nums):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1]=nums[j]
            i+=1
    return i+1

# another solution with the same approach 
def remove_duplicates_v3(arr):
    # [1,2,3,3]
    
    if not arr:
        return arr
    # Initialize variables
    write_index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is not equal to the previous element
        if arr[i] != arr[i - 1]:
            # If different, copy the current element to the write_index position
            arr[write_index] = arr[i]
            write_index += 1

    # Return a slice of the array containing only unique elements
    return write_index 


## another approach but it doesn't remove the duplicates IN PLACE 
def removeDuplicates_v4(nums ): 
    seen = set()
    unique_elements = []
    for num in nums: 
        if num not in seen: 
            seen.add(num)
            unique_elements.append(num)
    
    return unique_elements


arr = [1,1,2]
arr = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(arr))
# answer = removeDuplicates_v3(arr)
answer = removeDuplicates_v4()(arr)
print(answer)
# print(len(answer))
print(arr)