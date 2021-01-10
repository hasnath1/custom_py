# Bismillah {BY THE NAME OF ALLAH .}

#func : 1
# This function converts a string into a list .
def toList(string):
    a = string        # For easy-use .
    i = 0             # Starting point of the string 
    c_list = []       # This will store the characters in the string
    while i < len(a):
        c_list.append(a[i])
        i += 1

    return c_list     # At last return the value (list) ..

# Same copy of function 1 just a the below code is better version .
# func : 2
def toLst(str):
    list_a = []
    for i in str:
        list_a.append(i)
        
    return list_a


    



