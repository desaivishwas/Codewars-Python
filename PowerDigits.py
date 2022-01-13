def dig_pow(n, p):
    # your code
    a, res = str(n), 0
    for i in range(len(a)):
        res += (int(a[i]) ** (p+i))
    return res / n if res % n == 0 else -1
