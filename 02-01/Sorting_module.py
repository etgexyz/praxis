def  select_sort(arr):
    
    n = len(arr)
    
    for i in range(n-1,0,-1):
        Max = 0
        for lokasi in range(1, i+1):
            if arr[lokasi] > arr[Max]:
                Max = lokasi
        
        temp = arr[i]
        arr[i] = arr[Max]
        arr[Max] = temp
        print (arr)
    print(arr)
    
    #return arr

def insert_sort(arr):
    for i in range(1, len(arr)):
        actVal = arr[i]
        loc = i

        while loc > 0 and arr[loc-1] > actVal:
            arr[loc] = arr[loc-1]
            loc = loc -1
        
        arr[loc] = actVal

    return arr

def bubblesort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr