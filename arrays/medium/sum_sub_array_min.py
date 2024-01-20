def sumSubarrayMins(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    sum = 0
    for i in range(len(arr)): 
        for j in range(i+1, len(arr)+1):                                        
            sub = arr[i:j]
            min = 400000
            for num in sub: 
                if  num < min :
                    min = num
            sum += min
    return sum


def sumSubarrayMins_v2(arr):
    MOD = 10**9 + 7
    n = len(arr)
    result = 0
    stack = []

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result = (result + arr[j] * (i - j) * (j - k)) % MOD

        stack.append(i)

    while stack:
        j = stack.pop()
        k = stack[-1] if stack else -1
        result = (result + arr[j] * (n - j) * (j - k)) % MOD

    return result

# Example usage:
arr = [3,1,2,4]
print(sumSubarrayMins(arr))
print(sumSubarrayMins_v2(arr))