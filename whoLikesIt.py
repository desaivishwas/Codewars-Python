def likes(names):
    # your code here
    count = len(names) - 2
    if len(names) > 0 :
        if len(names) == 1:
            return f"{names[0]} likes this"
        if len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        if len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        if len(names) >=4:
            return f"{names[0]}, {names[1]} and {count} others like this"
    return "no one likes this"