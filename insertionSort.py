def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    
    

if __name__=='__main__':
    nums = [13,-3,-25,20,-3,-16,-23,18,20,0,12,-5,-22,15,-4,7]
    insertionSort(nums)
    print(nums)