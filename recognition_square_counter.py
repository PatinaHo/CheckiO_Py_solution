### Island: Scientific Expedition. Problem: The Square Chest

"""
My answer. Demerit: Unextendible.
"""
from typing import List

def checkio(line_list: List[List[int]]) -> int:
    line_listOfTuples = []
    for elem in line_list:
        line_listOfTuples.append(tuple(sorted(elem)))
    lines_set = set(line_listOfTuples)

    square_count = 0
    for x in range(1, 17):
        if(x % 4 != 0):
            if((x, x+1) in lines_set):
                if((x, x+4) in lines_set):
                    if((x+1, x+5) in lines_set):
                        if((x+4, x+5) in lines_set):
                            square_count += 1
                    if((x+1, x+2) in lines_set):
                        if((x+4, x+8) in lines_set):
                            if((x+2, x+6) in lines_set and (x+6, x+10) in lines_set):
                                if((x+8, x+9) in lines_set and (x+9, x+10) in lines_set):
                                    square_count += 1
                            if((x+2, x+3) in lines_set):
                                if((x+8, x+12) in lines_set):
                                    if((x+3, x+7) in lines_set and (x+7, x+11) in lines_set and (x+11, x+15) in lines_set):
                                        if((x+12, x+13) in lines_set and (x+13, x+14) in lines_set and (x+14, x+15) in lines_set):
                                            square_count += 1
    
    return square_count

