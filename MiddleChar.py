def get_middle(s):
    #your code here
    mid =  len(s) // 2
    if len(s) % 2 == 0:  
        return f"{s[mid -1]}{s[mid]}"
    return f"{s[mid]}"
    