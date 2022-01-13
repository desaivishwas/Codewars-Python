def high_and_low(numbers):
    # ...
    num = numbers.split()
    obj = map(int, num)
    num_list = list(obj)
    low, high = num_list[0], num_list[0]
    
    for i in range(1, len(num_list)-1):
        if num_list[i] < num_list[i + 1]:
            low = min(low, num_list[i])
            high = max(high, num_list[i + 1])
            
    result = f"{high} {low}"
    return result