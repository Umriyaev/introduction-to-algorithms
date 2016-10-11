def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    
  
  
def merge(nums, start, middle, end):
    left = start
    right = middle+1
    temp = []
    while left<=middle and right<=end:
        if nums[left]>nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while left<=middle:
        temp.append(nums[left])
        left+=1
    while right<=end:
        temp.append(nums[right])
        right+=1
    for i in range(0,len(temp)):
        nums[start+i]=temp[i]
    
    return nums
    
def mergeSort(nums, start, end):
    if start<end:
        middle = (start+end)//2
        nums = mergeSort(nums, start, middle)
        nums = mergeSort(nums, middle+1, end)
        nums = merge(nums, start, middle, end)
    return nums

def sort(nums):
    return mergeSort(nums, 0, len(nums)-1)

if __name__=='__main__':
    nums = [13,-3,-25,20,-3,-16,-23,18,20,0,12,-5,-22,15,-4,7]
    nums = sort(nums)
    print(nums)