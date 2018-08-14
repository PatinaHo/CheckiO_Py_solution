### Island: Electronic station. Problem: Brackets

class Stack:
    def __init__(self, expression=''):
        self.expression = expression
    
    def push(self, expression):
        self.expression = self.expression + expression
        
    def pop(self):
        elem = self.expression[-1]
        self.expression = self.expression[:-1]
        return elem
    
    def isEmpty(self):
        if (self.expression == ''):
            return True
        else:
            return False        
    
def checkio(expression):
    brac_pair = {')': '(', ']': '[', '}': '{'}
    left_brac_set = {'(', '[', '{'}
    right_brac_set = {')', ']', '}'}
    contains_brac = False
    
    bracket_stack = Stack()
    for char in expression:
        if(char in left_brac_set or char in right_brac_set):
            contains_brac = True
            break
    if (contains_brac) == False:
        return True
    
    for char in expression:
        if char in left_brac_set:
            bracket_stack.push(char)
        elif char in right_brac_set:
            if(bracket_stack.isEmpty() == True):
                return False
            else:
                left = bracket_stack.pop()
                if (left != brac_pair[char]):
                    return False
    if(bracket_stack.isEmpty()):
        return True
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"