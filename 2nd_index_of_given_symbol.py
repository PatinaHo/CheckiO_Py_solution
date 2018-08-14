### Island: Elementary. Problem: Second Index

"""
My answer.
"""

def second_index(text: str, symbol: str):  # -> [int, None]
    """
        returns the second index of a symbol in a given text
    """
    OCCURENCE = 2
    position = []
    
    for i, _ in enumerate(text):
        if(text[i] == symbol):
            position.append(i)
    
    if len(position) >= OCCURENCE:
        return position[OCCURENCE - 1]
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
