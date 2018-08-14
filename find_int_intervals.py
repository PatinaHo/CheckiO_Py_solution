### Island: Elementary. Problem: Create intervals

"""
My answer.
"""
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    sort_data = sorted(list(data))
    ans = []
    if(len(data) > 1):
        left = sort_data[0]
        tmp = left
        counter = 1
        right = sort_data[counter]
        while(counter < len(sort_data)):
            if(right == tmp + 1):
                tmp = right
            else:
                ans.append((left, tmp))
                left = right
                tmp = right
            counter += 1
            if(counter < len(sort_data)):
                right = sort_data[counter]
            elif(counter == len(sort_data)):
                ans.append((left, tmp))
    
    elif(len(data) == 1):
        elem = data.pop()
        ans.append((elem, elem))
            
    return ans 



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 4, 5, 6, 7, 8}) == [(1, 8)], "Second"
