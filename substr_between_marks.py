### Island: Elementary. Problem: Between Markers

"""
My answer.
"""

def between_markers(text: str, begin: str, end: str):  # -> str
    """
        returns substring between two given markers
    """
    begin_pos = text.find(begin)
    end_pos = text.find(end)
    
    if (begin_pos != -1 and end_pos != -1 and begin_pos < end_pos):
        return text[begin_pos + len(begin) : end_pos]
    elif (begin_pos == -1 and end_pos != -1):
        return text[0: end_pos]
    elif (begin_pos != -1 and end_pos == -1):
        return text[begin_pos + len(begin) :]
    elif(begin_pos == -1 and end_pos == -1):
        return text
    elif (begin_pos != -1 and end_pos != -1 and begin_pos > end_pos):
        return ''
