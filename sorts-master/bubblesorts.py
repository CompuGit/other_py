def bubblesort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>= arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]

def combsort(arr):
    pass

def exchangesort(arr):
    pass

if __name__ == '__main__':

    from timeit import timeit

    lst = [3,5,7,2,5,1,4,9,8,0]
    print('unsorted list :',lst)
    bubblesort_time = timeit(stmt='bubblesort(lst)', globals=globals(), number=1)

    print('bubble sorted list :',lst)
    print('execution time : %.16f micro sec'%(bubblesort_time*1000000), end='\n\n')