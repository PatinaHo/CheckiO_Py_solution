### Island: O'Reilly. Problem: Cipher Map

def recall_password(cipher_grille, ciphered_password):
    """
    Given an integer value and return a roman numeral system number, which combines
    """
    
    result = []    
    rotation_times = 0
    
    while rotation_times < 4:
        for x,y in list(zip(cipher_grille, ciphered_password)):
            j = -1
            for i in x:
                j += 1
                if i == "X":
                    result.append(y[j])
                elif i == ".":
                    continue
        cipher_grille = list(zip(*cipher_grille[::-1]))
        rotation_times += 1
        
    result = "".join(result)
    
    return result