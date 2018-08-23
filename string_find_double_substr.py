### Island: Scientific Expedition. Problem: Double Substring

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    group_size = int(len(line)/2)   # half of the line size is the largest size a substring could be
                                    # check each combination of that size, and decrease the size until two identicle substring is found
    while(group_size >= 1):
        left_start = 0
        right_start = left_start + group_size
        while(left_start <= len(line) - 2*group_size):
            while(right_start <= len(line) - group_size):
                left_group = line[left_start : left_start + group_size]
                right_group = line[right_start : right_start + group_size]
                if(left_group == right_group):
                    break
                right_start += 1
            if(left_group == right_group):
                break
            left_start += 1
            right_start = left_start + group_size
        if(left_group == right_group):
            break
        group_size -= 1
    
    return group_size



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
