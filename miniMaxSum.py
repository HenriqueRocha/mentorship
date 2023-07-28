def miniMaxSum(arr):
    minSum = float('inf')
    maxSum = float('-inf')
    totalSum = sum(arr)

    for num in arr:
        currentSum = totalSum - num
        minSum = min(minSum, currentSum)
        maxSum = max(maxSum, currentSum)

    print(minSum, maxSum)




