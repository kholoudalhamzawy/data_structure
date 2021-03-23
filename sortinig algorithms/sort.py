
import binary_tree
def buble(list):
    for index1 in range (len(list)-1) :
        for index2 in range ((len(list)-1)-index1):
            if list[index2]>list[index2+1] :
               list[index2],list[index2+1]=list[index2+1],list[index2]
    return list

def selection(list):
    for index1 in range (len(list)) :
        item_to_insert = list[index1]
        index_to_insert=index1
        for index2 in range(index1 +1,len(list)):
            if item_to_insert > list[index2]:
                item_to_insert = list[index2]
                index_to_insert = index2
        list[index1],list[index_to_insert]=item_to_insert,list[index1]

    return list


def insertion(list):
    for index1 in range(1, len(list)):
        item_to_insert = list[index1]
        index2 =index1-1
        while index2 >= 0 and list[index2] > item_to_insert:
            list[index2+1] = list[index2]
            index2 -= 1
        list[index2+1] = item_to_insert

    return list


#kossom elmerge

def merge(list):
    if len(list)>1:
        middle_index=len(list)//2
        left_arr=[]
        right_arr=[]
        for index in range (len(list)):
            if index<middle_index:
                left_arr.append(list[index])
            else:
                right_arr.append(list[index])
        list.clear()
        merge(left_arr)
        merge(right_arr)

        left_arr_len=right_arr_len=0
        for index in range(len(left_arr)+len(right_arr)):
            if left_arr_len>=middle_index:
                list.append(right_arr[right_arr_len])
                right_arr_len += 1

            elif right_arr_len>=(len(left_arr)+len(right_arr))-middle_index:
                list.append(left_arr[left_arr_len])
                left_arr_len += 1

            elif left_arr[left_arr_len]>right_arr[right_arr_len]:
                list.append(right_arr[right_arr_len])
                right_arr_len += 1

            else :
                list.append(left_arr[left_arr_len])
                left_arr_len+=1

        return list



def partition(list,start,end):
    pivot=end
    for index in range(end-1,start-1,-1):
        if list[index]>=list[end]:
            pivot-=1
            list[pivot],list[index]=list[index],list[pivot]
    list[pivot],list[end]=list[end],list[pivot]
    return pivot

def quick(list,start,end):
    if start<end:
        pivot=partition(list,start,end)
        quick(list,start,pivot-1)
        quick(list,pivot+1,end)
    return list

def binary(list):
    tree=binary_tree.binary_tree()
    for item in list:
        tree(item)
    return tree.sorted_tree()


#comparing the index with its parents from top to bottom every time
def max_heap(list):
    for index in range(1,len(list)):
        if index/2 > index//2:
            parent_index=((index//2) +1)-1
        else:
            parent_index=(index//2)-1
        while parent_index>=0 :
            if list[index] > list[parent_index]:
                list[index],list[parent_index]=list[parent_index],list[index]
                if not parent_index:
                    break
                index=parent_index
                if parent_index / 2 > parent_index // 2:
                    parent_index = ((parent_index // 2) + 1) - 1
                else:
                    parent_index = (parent_index // 2) - 1
            else:
                break
    return list


def heap(list):
    max_heap(list)
    for last_index in range(len(list)-1,0,-1):
        list[0], list[last_index] = list[last_index], list[0]
        list[:last_index]=max_heap(list[:last_index])
    return list



#comparing the index with its children from the bottom to the top in the build of the first max heap
#then comparing the root with its children everytime a swap happens
def heapify(list,len,index):
    maxx=index
    l=2*index+1
    r=2*index+2

    if l<len and list[index]<list[l]:
        maxx=l

    if r<len and list[maxx]<list[r]:
        maxx=r

    if maxx !=index:
        list[index],list[maxx]=list[maxx],list[index]
        heapify(list,len,maxx)

def heap_sort(arr):
    length=len(arr)
    #to build a max heap we start from the bottom to the root
    #same as was built in the maxheap function
    for i in range(length//2,-1,-1):
        heapify(arr,length,i)
    #to keep building max heaps we start from the root to get the next max element again to the root
    # and get the element wich was just swapped to the bottom or its right place
    for i in range(length-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr









if __name__== '__main__':
    print(buble([3,4,2,8,3,5,1]))
    print(selection([3, 4, 2, 8, 3, 4, 1]))
    print(insertion([3, 4, 2, 8, 3, 4, 1]))
    print(merge([3, 4, 2, 8, 3, 4, 1]))
    print(binary([3, 4, 2, 8, 3, 4, 1]))
    print(quick([3, 4, 2, 8, 3, 4, 1],0,6))
    print(heap([3, 4, 2, 8, 3, 4, 1]))
    print(heap_sort([3, 4, 2, 8, 3, 4, 1]))
