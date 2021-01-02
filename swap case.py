def swap_case(s):
    x="" # to keep the changed character have to take a empty string
    for c in s: #to access all the elements in the string
        if c.isupper(): #if the char is in uppercase
            c=c.lower() #change it to lowercase
        else:
            c=c.upper() #change it to upper   
        x+="".join(c) # join the element
    return x
    #return s.swapcase() # alternative way