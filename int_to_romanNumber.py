### Island: Electronic station. Problem: Roman Numerals

RomanNum_Symbol={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

def checkio(data):
    """
    Given an integer value and return a Roman numeral system number using Roman number symbols.
    """

    RomanNum = ""
    i=0
    
    while int(data/pow(10,i)) >0:
        i+=1
    
    while i >0:
        #append symbols when data includes 5*pow(10,n)
        a = data % pow(10,i)
        b = 5*pow(10,i-1)
        if int( a / b) == 1 :
            e = str(RomanNum_Symbol[5*pow(10,i-1)])
            RomanNum= RomanNum+e
            
        #append the rest part exluding 5*pow(10,n)
        d= (data % pow(10,i)) % (5*pow(10,i-1))
        g = 0
        while d >= pow(10,i-1):
            f = str(RomanNum_Symbol[pow(10,i-1)])
            RomanNum= RomanNum + f
            g += 1
            d-= pow(10,i-1)
            
            if int(a/b)==0 and g == 4:
                h=str(RomanNum_Symbol[5*pow(10,i-1)])
                RomanNum= RomanNum[:-3]
                RomanNum= RomanNum + h
            elif int(a/b)==1 and g == 4:
                j=str(RomanNum_Symbol[pow(10,i)])
                RomanNum= RomanNum[:-5]
                RomanNum= RomanNum + f + j
            
            
        i-=1
    
    return RomanNum