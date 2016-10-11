def findCrossingMaxSubarray(nums, low, mid, high):
    leftSum = -100000000000
    currentSum = 0
    leftIndex = None
    for i in range(mid, low-1, -1):
        currentSum+=nums[i]
        if currentSum>leftSum:
            leftSum = currentSum
            leftIndex = i
    rightSum = -1000000000000
    currentSum = 0
    rightIndex = None
    for j in range(mid+1, high+1):
        currentSum+=nums[j]
        if currentSum>rightSum:
            rightSum = currentSum
            rightIndex = j
    return leftIndex, rightIndex, leftSum+rightSum
    
def findMaxSubarray(nums, low, high):
    if low==high:
        return low, high, nums[low]
    else:
        mid = (low+high)//2
        leftStart, leftEnd, leftSum = findMaxSubarray(nums, low, mid)
        rightStart, rightEnd, rightSum = findMaxSubarray(nums, mid+1, high)
        crossStart, crossEnd, crossSum = findCrossingMaxSubarray(nums, low, mid, high)
        if leftSum>rightSum and leftSum>crossSum:
            return leftStart, leftEnd, leftSum
        elif rightSum>leftSum and rightSum>crossSum:
            return rightStart, rightEnd, rightSum
        else:
            return crossStart, crossEnd, crossSum
    
def maxSubArray(nums):
    return findMaxSubarray(nums, 0, len(nums)-1)
if __name__=='__main__':
    nums = [10,15,20,25,30,-10,20,-10,-30,-20]
    maxStart, maxEnd, maxSum = maxSubArray(nums)
    print("(%i, %i): %i" % (maxStart, maxEnd, maxSum))
    
