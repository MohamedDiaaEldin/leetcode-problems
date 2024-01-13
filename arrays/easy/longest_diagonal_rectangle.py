'''
u are given a 2D 0-indexed integer array dimensions.

For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

 

Example 1:

Input: dimensions = [[9,3],[8,6]]
Output: 48
Explanation: 
For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.
Example 2:

Input: dimensions = [[3,4],[4,3]]
Output: 12
Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.
 

Constraints:

1 <= dimensions.length <= 100
dimensions[i].length == 2
1 <= dimensions[i][0], dimensions[i][1] <= 100

'''


import math
def areaOfMaxDiagonal(dimensions):
    greater_diagonal = 0    
    greater_area = 0
    for i in range(len(dimensions)): 
        diagonal = math.sqrt(dimensions[i][0] ** 2 + dimensions[i][1] ** 2)
        # print('current is : ', diagonal, ' with index : ', i , ' area is :', dimensions[i][0] * dimensions[i][1])
        if diagonal >= greater_diagonal :
            if diagonal == greater_diagonal :
                greater_area = max(greater_area, dimensions[i][0] * dimensions[i][1])                    
            else : 
                greater_area = dimensions[i][0] * dimensions[i][1]
                greater_diagonal = diagonal

    return greater_area
def areaOfMaxDiagonal_v3(dimensions):
    greater_diagonal = 0    
    greater_area = 0
    for width, height in dimensions: 
        diagonal = math.sqrt(width ** 2 + height ** 2)        
        if diagonal >= greater_diagonal :
            if diagonal == greater_diagonal :
                greater_area = max(greater_area, width * height)                    
            else : 
                greater_area = width * height
                greater_diagonal = diagonal

    return greater_area




def areaOfMaxDiagonal_v2( dimensions):
    """
    :type dimensions: List[List[int]]
    :rtype: int
    """
    n = len(dimensions)
    ans = 0
    d = 0
    for i in range(n):
        t = (dimensions[i][0]**2 + dimensions[i][1]**2)**0.5
        
        if t >= d:
            if t==d:
                ans = max(ans,dimensions[i][0]*dimensions[i][1])
            else:
                ans = dimensions[i][0]*dimensions[i][1]
            d = t
    return ans

dimensions = [[2,6],[5,1],[3,10],[8,4]]
# dimensions = [[4,7],[8,9],[5,3],[6,10],[2,9],[3,10],[2,2],[5,8],[5,10],[5,6],[8,9],[10,7],[8,9],[3,7],[2,6],[5,1],[7,4],[1,10],[1,7],[6,9],[3,3],[4,6],[8,2],[10,6],[7,9],[9,2],[1,2],[3,8],[10,2],[4,1],[9,7],[10,3],[6,9],[9,8],[7,7],[5,7],[5,4],[6,5],[1,8],[2,3],[7,10],[3,9],[5,7],[2,4],[5,6],[9,5],[8,8],[8,10],[6,8],[5,1],[10,8],[7,4],[2,1],[2,7],[10,3],[2,5],[7,6],[10,5],[10,9],[5,7],[10,6],[4,3],[10,4],[1,5],[8,9],[3,1],[2,5],[9,10],[6,6],[5,10],[10,2],[6,10],[1,1],[8,6],[1,7],[6,3],[9,3],[1,4],[1,1],[10,4],[7,9],[4,5],[2,8],[7,9],[7,3],[4,9],[2,8],[4,6],[9,1],[8,4],[2,4],[7,8],[3,5],[7,6],[8,6],[4,7],[25,60],[39,52],[16,63],[33,56]]
print(areaOfMaxDiagonal(dimensions))
print('version 2')
print(areaOfMaxDiagonal_v2(dimensions))
print('version 3')
print(areaOfMaxDiagonal_v3(dimensions))
