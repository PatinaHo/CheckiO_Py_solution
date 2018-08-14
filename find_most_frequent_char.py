### Island: Home. Problem: The most wanted letter

def checkio(text: str):
    """ Find the most frequent letter in the text; if two or more letters with the same frequency, return the one comes first in latin alphabet order.
    alphabet_dict: A dictionary of words(key) appeared in text, and how many times(value) each had appeared.

    """

    alphabet_dict = {}
    
    for char in text.lower():
        if char.isalpha():
            if char in alphabet_dict:
                alphabet_dict[char] += 1
            else:
                alphabet_dict[char] = 1
    
    max_count = max(alphabet_dict.values())
    max_count_items = 0
    max_count_items_set = set()
    
    for _ in alphabet_dict:
        if (alphabet_dict[_] == max_count):
            max_count_items += 1
            max_count_items_set.add(_)
    
    if (max_count_items == 1):
        return max(alphabet_dict, key=alphabet_dict.get)
    else:
        return min(max_count_items_set)



if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."