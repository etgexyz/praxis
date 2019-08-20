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
    
    return arr