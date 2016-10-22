def hoarePartition(A, start, end):
    x = A[start]
    i = start-1
    j = end+1
    while True:
        while True:
            j-=1
            if A[j]<=x:
                break
        while True:
            i+=1
            if A[i]>=x:
                break
        if i<j:
            buf = A[i]
            A[i]=A[j]
            A[j]=buf
        else:
            return j
 
def quickSort(A, start, end):
    while start<end:
        pivot = hoarePartition(A, start, end)
        quickSort(A, start, pivot)
        start = pivot+1
            
if __name__=='__main__':
    nums = [13,19,9,5,12,8,7,4,11,2,6,21]
    j = quickSort(nums, 0, len(nums)-1)
    print(j)
    print(nums)
