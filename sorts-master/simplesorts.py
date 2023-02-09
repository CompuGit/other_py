def selectionsort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>=arr[j]:
                arr[i],arr[j] = arr[j],arr[i]


def insertionsort(arr):
    for i in range(1,len(arr)):
        j = i-1
        while arr[j]>arr[j+1] and j>=0:
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j-=1

if __name__ == '__main__':

    from timeit import timeit

    lst = [3,5,7,2,5,1,4,9,8,0]
    print('unsorted list :',lst)
    selectionsort_time = timeit(stmt='selectionsort(lst)', globals=globals(), number=1)

    print('selection sorted list :',lst)
    print('execution time : %.16f micro sec'%(selectionsort_time*1000000), end='\n\n')

    lst = [3,5,7,2,5,1,4,9,8,0]
    print('unsorted list :',lst)
    insertionsort_time = timeit(stmt='insertionsort(lst)', globals=globals(), number=1)

    print('insertion sorted list :',lst)
    print('execution time : %.16f micro sec'%(insertionsort_time*1000000), end='\n\n')