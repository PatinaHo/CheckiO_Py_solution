
### Island: O'Reilly. Problem: Median

from typing import List

def checkio(data: List[int]): # -> [int, float]
    def Qsort(data):
        data_copy = data
        pk = 0
        i = 1
        j = len(data) - 1
        pk_switch = 0
        # print("Beginning of Qsort =", data[0])
        while(i < j and i <= len(data) and j > pk):
            while(data[i] <= data[pk] and i < len(data)-1):
                i = i+1;
            while(data[j] >= data[pk] and j > pk+1):
                j = j-1;
            if(i < j):
                data_copy[i], data_copy[j] = data[j], data[i];
        if (i >= j and data_copy[pk] > data_copy[j]):
            data_copy[pk], data_copy[j] = data_copy[j], data_copy[pk];
            pk_switch = 1
        if(j > 1):
            data_copy[:j] = Qsort(data_copy[:j])
        if(j < len(data) - 1):
            if(pk_switch == 1):
                data_copy[j+1:] = Qsort(data_copy[j+1:])
            else:
                data_copy[j:] = Qsort(data_copy[j:])
        return data_copy
    
    sorted_data = Qsort(data)
    item_num = len(sorted_data)
    index = int(item_num/2)
    if(item_num % 2 == 0):
        # print("even length, ans =", (sorted_data[index - 1] + sorted_data[index]) / 2)
        # for item in sorted_data:
        #     print(item, sep='', end=' ')
        return (sorted_data[index - 1] + sorted_data[index]) / 2
    else:
        return sorted_data[index]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")