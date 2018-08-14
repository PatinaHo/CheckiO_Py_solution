def Qsort(data):
    """Return List of data_copy which is sorted. 
       This Qsort isn't yet improved; its worst case is still O(n^2)"""

    data_copy = data
    pk = 0
    i = 1
    j = len(data) - 1
    pk_switch = 0
    # print("Beginning of Qsort =", data[0])
    
    # Partition
    while(i < j and i <= len(data) and j > pk):
        while(data[i] <= data[pk] and i < len(data)-1):
            i = i+1;
        while(data[j] >= data[pk] and j > pk+1):
            j = j-1;
        if(i < j):
            data_copy[i], data_copy[j] = data[j], data[i];
    
    # Swap pivot key
    if (i >= j and data_copy[pk] > data_copy[j]):
        data_copy[pk], data_copy[j] = data_copy[j], data_copy[pk];
        pk_switch = 1
    
    # Recursion
    if(j > 1):
        data_copy[:j] = Qsort(data_copy[:j])
    if(j < len(data) - 1):
        if(pk_switch == 1):
            data_copy[j+1:] = Qsort(data_copy[j+1:])
        else:
            data_copy[j:] = Qsort(data_copy[j:])
    return data_copy