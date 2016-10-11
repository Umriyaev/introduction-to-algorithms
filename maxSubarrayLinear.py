def maximumSubarray(nums):
    maxSoFar = 0
    maxEndingHere = 0
    maxStart=0
    maxEnd = 0
    for i in range(0, len(nums)):
        maxEndingHere+=nums[i]
        if maxEndingHere<0:
            maxEndingHere = 0
            maxStart = maxEnd = i+1
        if maxEndingHere>maxSoFar:
            maxSoFar = maxEndingHere
            maxEnd = i
    return maxStart, maxEnd, maxSoFar


def maximumSubarrayNonEmpty(nums):
    maxSoFar = maxEndingHere = nums[0]
    maxStart = 0
    maxEnd = 0
    for i in range(1, len(nums)):
        if maxEndingHere+nums[i]<nums[i]:
            maxStart = i
            maxEndingHere = nums[i]
        else:
            maxEndingHere+=nums[i]
        if maxSoFar<maxEndingHere:
            maxEnd = i
            maxSoFar = maxEndingHere
    return maxStart, maxEnd, maxSoFar
    

if __name__=='__main__':
    nums = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    maxStart, maxEnd, maxSum = maximumSubarray(nums)
    print("(%i, %i): %i" % (maxStart, maxEnd, maxSum))
    
    nums2 = [-1,-2, 2,-1,20,-5]
    maxStart, maxEnd, maxSum = maximumSubarrayNonEmpty(nums2)
    print("(%i, %i): %i" % (maxStart, maxEnd, maxSum))