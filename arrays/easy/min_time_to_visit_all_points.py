def minTimeToVisitAllPoints_v1( points):
        if len(points) < 2: 
            return 0
        total = 0
        for i in range(len(points)-1): 
            point1 = points[i]
            point2 = points[i+1]
            y = abs(point1[1] - point2[1])
            x = abs(point1[0] - point2[0]   )
            time = y if y > x else x
            total += time
        return total



# Example usage:
# points = [[1, 1], [3, 4], [-1, 0]]
# result = minTimeToVisitAllPoints_v1(points)
# print("Minimum time to visit all points:", result)


def minTimeToVisitAllPoints(points):
    total_time = sum(max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
                     for i in range(len(points) - 1))
    
    return total_time

# Example usage:
points = [[1, 1], [3, 4], [-1, 0]]
result = minTimeToVisitAllPoints(points)
print("Minimum time to visit all points:", result)


