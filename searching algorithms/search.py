
import sort
import math

# jump search is better than binary serach when it comes to large numbers because it doesn't rely om the '/' operator which is expensive
# to reduce the linear time we could use the binary serach instead
def jump(arr,size,x):
    arr=sort.binary(arr)
    step=int(math.sqrt(size))
    # if size was a prime number and didn't had a sqrt, so when adding, it may exceed the size
    while arr[int(min(step,size))-1]<x:
        if step>= size:
            return -1
        step+=int(math.sqrt(size))

    for index in range (int(step-math.sqrt(size)),step+1):
        if arr[index-1]==x:
            return index
    return -1










if __name__=='__main__':
    print("k")
