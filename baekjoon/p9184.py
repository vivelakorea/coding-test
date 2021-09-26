cache = {}
def p9184(a, b, c):
    def cache_check_and_return(a, b, c):
        if (a, b, c) in cache:
            return cache[(a, b, c)]
        tmp = p9184(a, b, c)
        cache[(a, b, c)] = tmp
        return tmp

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return cache_check_and_return(20, 20, 20)

    if a < b and b < c:
        return cache_check_and_return(a, b, c-1) + cache_check_and_return(a, b-1, c-1) - cache_check_and_return(a, b-1, c)

    else:
        return cache_check_and_return(a-1, b, c) + cache_check_and_return(a-1, b-1, c) + cache_check_and_return(a-1, b, c-1) - cache_check_and_return(a-1, b-1, c-1)

while True:
    a, b, c = map(int, input().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, p9184(a, b, c)))