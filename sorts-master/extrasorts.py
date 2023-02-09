def mysort(arr):
    for i in range(len(arr)):
        mn = min(arr)
        arr.remove(mn)
        arr.insert(i,mn)

if __name__ == '__main__':

    from timeit import timeit

    lst = [3,5,7,2,5,1,4,9,8,0]
    print('unsorted list :',lst)
    mysort_time = timeit(stmt='mysort(lst)', globals=globals(), number=1)

    print('my sorted list :',lst)
    print('execution time : %.16f micro sec'%(mysort_time*1000000), end='\n\n')
