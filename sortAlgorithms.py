#*************merge sort***************************
def mergeSort(array, start, end):
    if start<end:
        middle = (start+end)//2
        mergeSort(array, start, middle)
        mergeSort(array, middle+1, end)
        merge(array, start, middle, end)
        
def merge(nums, start, middle, end):
    buf = []
    left = start
    right = middle+1
    
    while left<=middle and right<=end:
        if nums[left]<nums[right]:
            buf.append(nums[left])
            left+=1
        else:
            buf.append(nums[right])
            right+=1
    while left<=middle:
        buf.append(nums[left])
        left+=1
    while right<=end:
        buf.append(nums[right])
        right+=1
    for i in range(0, len(buf)):
        array[start+i]=buf[i]
#****************************************************


#*******************quicksort************************
def partition(array, start, end):
    i = -1
    pivot = array[end]
    for j in range(0, end):
        if array[j]<=pivot:
            i+=1
            buf = array[j]
            array[j]=array[i]
            array[i]=buf
    buf = array[i+1]
    array[i+1]=array[end]
    array[end]=buf
    return i+1
    
def quicksort(array, start, end):
    if start<end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)

#****************************************************

#*******************heapsort*************************
def leftChild(index):
    return (index<<1)+1
def rightChild(index):
    return (index<<1)+2
def parent(index):
    return (index-1)>>1

def maxHeapify(array, index, heapSize):
    left = leftChild(index)
    right = rightChild(index)
    
    maxIndex = index
    if left<heapSize and array[left]>array[index]:
        maxIndex = left
    if right<heapSize and array[right]>array[maxIndex]:
        maxIndex = right
    while maxIndex!=index:
        buf = array[maxIndex]
        array[maxIndex] = array[index]
        array[index]=buf
        index = maxIndex
        left = leftChild(index)
        right = rightChild(index)
        if left<heapSize and array[left]>array[index]:
            maxIndex = left
        else:
            maxIndex = index
        if right<heapSize and array[right]>array[maxIndex]:
            maxIndex = right

def buildMaxHeap(array):
    for i in range(len(array)//2, -1, -1):
        maxHeapify(array, i, len(array))

def heapSort(array):
    buildMaxHeap(array)
    heapSize = len(array)
    while heapSize>0:
        buf = array[heapSize-1]
        array[heapSize-1]=array[0]
        array[0]=buf
        heapSize -= 1
        maxHeapify(array, 0, heapSize)
#*******************************************************        
def sort(array):
    heapSort(array)
    
if __name__=='__main__':
    array = [3,5,6,7,4,3,2,2,4,6,7,5,2,5,67,8,98,76,5,4,3,2,5,67]
    sort(array)
    print(array)
