### Island: Electronic station. Problem: Long Repeat Inside

def principal_period(s):
    """
        return the repeating substring in s
    """
    i = (s+s).find(s, 1, -1)
    if i == -1:
        return None
    else:
        return s[:i]

def repeat_inside(line):
    """
        first the longest repeating substring
    """
    for tail in range(len(line)-1, 0, -1):
        for head in range(len(line)-tail):
            if (principal_period(line[head : tail + head+1])):  # start from the largest, gradually downsize the substring
                                                                # once a repeating sub-substring is found in substring, return the substring
                return line[head: tail+head+1]
    return ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"