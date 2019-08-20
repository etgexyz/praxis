def insert_sort(arr):
    for i in range(1, len(arr)):
        actVal = arr[i]
        loc = i

        while loc > 0 and arr[loc-1] > actVal:
            arr[loc] = arr[loc-1]
            loc = loc -1
        
        arr[loc] = actVal

    return arr