def leftChild(i):
    return (i << 1) + 1
def rightChild(i):
    return (i << 1) + 2
def parent(i):
    if i==0:
        return i
    else:
        return i>>1
        
def maxHeapifyNonRecursive(A, i):
    while True:
        largest = i
        left = leftChild(i)
        right = rightChild(i)
        if left<len(A) and A[left]>A[i]:
            largest = left
        if right<len(A) and A[right]>A[largest]:
            largest = right
        if largest == i:
            break
        else:
            buf = A[largest]
            A[largest] = A[i]
            A[i] = buf
            i = largest

        
def maxHeapify(A, i):
    left = leftChild(i)
    right = rightChild(i)
    largest = i
    if left < len(A) and A[left]>A[i]:
        largest = left
    else:
        largest = i
    if right < len(A) and A[right]>A[largest]:
        largest = right
    if largest!=i:
        buf = A[largest]
        A[largest] = A[i]
        A[i] = buf
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(len(A)//2, -1, -1):
        maxHeapifyNonRecursive(A, i)
    

def minHeapifyNonRecursive(A, i):
    while True:
        smallest = i
        left = leftChild(i)
        right = rightChild(i)
        if left < len(A) and A[left]<A[i]:
            smallest = left
        if right<len(A) and A[right]<A[smallest]:
            smallest = right
        if smallest==i:
            break
        else:
            buf = A[smallest]
            A[smallest]=A[i]
            A[i]=buf
            i = smallest

def minHeapify(A, i):
    left = leftChild(i)
    right = rightChild(i)
    smallest = i
    if left < len(A) and A[left]<A[i]:
        smallest = left
    else:
        smallest = i
    if right < len(A) and A[right]<A[smallest]:
        smallest = right
    if smallest!=i:
        buf = A[smallest]
        A[smallest]=A[i]
        A[i]=buf
        minHeapify(A, smallest)
        
def buildMinHeap(A):
    for i in range(len(A)//2, -1, -1):
        minHeapifyNonRecursive(A, i)

    
        

if __name__=='__main__':
    A = [4,3,2,12,4,5,67,7,5,3,5,15]
    buildMaxHeap(A)
    print(A)
    
    B = [4,3,2,12,4,5,67,7,5,3,5,15]
    buildMinHeap(B)
    print(B)
    
    