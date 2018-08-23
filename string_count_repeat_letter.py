### Island: Home. Problem: Long Repeat


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if (line == ''):
        return 0
    front = line[0]
    count = 1
    maximum = 1
    for char in line[1:]:
        if (char == front):
            count += 1
            if (count > maximum):
                maximum = count
        else:
            count = 1
        front = char

    return maximum



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
