#randomized implementation of quicksort
import random

def partition(array, start, end):
    i = -1
    pivot = array[end]
    for j in range(0, end):
        if array[j]<=pivot:
            i+=1
            buf = array[i]
            array[i]=array[j]
            array[j]=buf
    buf = array[end]
    array[end]=array[i+1]
    array[i+1]=buf
    return i+1

def randomizedPartition(array, start, end):
    index = random.randint(start, end)
    buf = array[index]
    array[index] = array[end]
    array[end]=buf
    return partition(array, start, end)
    
def randomizedQuicksort(array, start, end):
    if start<end:
        pivot = randomizedPartition(array, start, end)
        randomizedQuicksort(array, start, pivot-1)
        randomizedQuicksort(array, pivot+1, end)
        
def sort(array):
    randomizedQuicksort(array, 0, len(array)-1)
    
if __name__=='__main__':
    array = [2,3,5,6,4,3,2,1,-4,-5,5,6,7,8,5,3,2,3,5,6,1000,7]
    sort(array)
    print(array)