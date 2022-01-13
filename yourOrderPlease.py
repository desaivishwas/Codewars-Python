def order(sentence):
    l = list(sentence.split())
    dict_of_numbers = {"1":"", "2":"","3":"", "4":"", "5":"", "6":"","7":"", "8":"","9":""}
    for word in l:
        for num in word:
            if num.isdigit() and int(num) <= 9:
                dict_of_numbers[num] = word
    ans = ""
    for k,v in dict_of_numbers.items():
        if v != "":
            ans = ans + v +" "
    return ans[:-1]