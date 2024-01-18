'''

108. Convert Sorted Array to Binary Search Tree
Solved
Easy
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
binary search tree.


Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.


'''


## for testing 
def height(root):

	# base condition when binary tree is empty
	if root is None:
		return 0
	return max(height(root.left), height(root.right)) + 1

# function to check if tree is height-balanced or not


def isBalanced(root):

	# Base condition
	if root is None:
		return True

	# for left and right subtree height
	lh = height(root.left)
	rh = height(root.right)

	# allowed values for (lh - rh) are 1, -1, 0
	if (abs(lh - rh) <= 1) and isBalanced(
			root.left) is True and isBalanced(root.right) is True:
		return True

	# Why don't we use that 	
	# if (abs(lh - rh) <= 1) :
	# 	return True

	# if we reach here means tree is not
	# height-balanced tree
	return False

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    total_nums = len(nums)
    if not total_nums:
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node], 
        sortedArrayToBST(nums[:mid_node]), sortedArrayToBST(nums[mid_node + 1 :])
    )


        
        
nums = [-10,-3,0,5,9]
print(isBalanced(sortedArrayToBST(nums)))

