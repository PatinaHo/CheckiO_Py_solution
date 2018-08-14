### Island: O'Reilly. Problem: Long Non Repeat

def non_repeat(line):
    """ 
    the longest substring without repeating chars
    """
    longest_non_repeat = ''
    non_repeat = longest_non_repeat
    repetition = False
    for char in line:
        for char_nr in non_repeat:
            if (char == char_nr):
                repetition = True
                break
        non_repeat += char        
        if(repetition == False):
#             print(non_repeat, char)
            if(len(non_repeat) > len(longest_non_repeat)):
                longest_non_repeat = non_repeat
        else:
#             print("repetition occurs, char =",char)
            non_repeat = non_repeat[non_repeat.index(char)+1:]
#             print("after cutting, non_repeat =", non_repeat)
            repetition = False
    return longest_non_repeat


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('abcddefg') == 'abcd', "Fourth"